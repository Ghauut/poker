import random

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# Store connected players and game state
players = {}
game_state = {
    'deck': [],
    'community_cards': [],
    'pot': 0,
    'current_bet': 0,
    'player_hands': {}
}

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class PokerGame:
    def __init__(self):
        self.players = {}
        self.game_state = {
            'deck': self.create_deck(),
            'community_cards': [],
            'pot': 0,
            'current_bet': 0,
            'player_hands': {}
        }

    def create_deck(self):
        deck = [{'value': v, 'suit': s} for v in VALUES for s in SUITS]
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        for player in self.players:
            hand = [self.game_state['deck'].pop(), self.game_state['deck'].pop()]
            self.game_state['player_hands'][player] = hand

    async def broadcast(self, message: dict):
        for player in self.players.values():
            await player.send_json(message)


poker_game = PokerGame()


# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, player_id: str):
        await websocket.accept()
        self.active_connections.append((websocket, player_id))
        poker_game.players[player_id] = websocket

    def disconnect(self, websocket: WebSocket):
        self.active_connections = [(ws, pid) for ws, pid in self.active_connections if ws != websocket]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: dict):
        for websocket, _ in self.active_connections:
            await websocket.send_json(message)


manager = ConnectionManager()


@app.websocket("/ws/{player_id}")
async def websocket_endpoint(websocket: WebSocket, player_id: str):
    await manager.connect(websocket, player_id)
    await manager.broadcast({"message": f"Player {player_id} joined the game."})
    
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message from {player_id}: {data}")
            await handle_player_action(player_id, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast({"message": f"Player {player_id} left the game."})

async def handle_player_action(player_id: str, action: str):
    if action == 'start_game':
        poker_game.deal_cards()
        await poker_game.broadcast({"message": "Game started", "hands": poker_game.game_state['player_hands']})
    elif action.startswith('bet'):
        amount = int(action.split(':')[1])
        poker_game.game_state['pot'] += amount
        await poker_game.broadcast({"message": f"{player_id} bet {amount}", "pot": poker_game.game_state['pot']})