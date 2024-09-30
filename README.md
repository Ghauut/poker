# Multiplayer Poker Game

A simple multiplayer poker game built with **FastAPI**, **WebSocket**, and **JavaScript** for real-time interaction. This game implements the Texas Hold'em poker rules, allowing multiple players to join a single table, manage game phases, and engage in turn-based betting.

## Features

- **Real-time multiplayer**: Players can join the game and interact in real time.
- **Game phases**: Supports Texas Hold'em phases: pre-flop, flop, turn, river, and showdown.
- **Turn-based betting**: Players take turns to place bets or fold.
- **Community cards and pot tracking**: Displays community cards and current pot size.
- **WebSocket communication**: Efficient real-time updates between server and clients.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI, WebSocket
- **Database**: None (atm)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Node.js (for frontend development)
- A modern web browser

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Ghauut/poker.git
   cd poker
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv .env
   source .env/bin/activate  # On Windows use `.env\Scripts\activate`
   ```

3. **Install dependencies**:

   Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Frontend Setup**:

   Ensure you have the frontend files (`index.html`, `styles.css`, and `script.js`) in a suitable directory (e.g., `frontend/`).

### Running the Server

1. **Start the FastAPI server**:

   ```bash
   uvicorn server:app --reload
   ```

   This will start the server at `http://127.0.0.1:8000`.

2. **Open the game in your browser**:

    Open `client.html`
   (Navigate to `http://127.0.0.1:8000` to view the game. Open multiple tabs to simulate different players.)

### Usage

1. **Join the game**: Each player needs to provide a unique player ID (e.g., Player1, Player2).
2. **Start the game**: Click the "Start Game" button to initiate gameplay.
3. **Betting**: Players can place bets, fold, or send chat messages using the provided buttons.
4. **Watch phases**: The game will display the current phase, community cards, and the pot size in real time.

## Development

### Contributing

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. All contributions are welcome!

### Future Improvements

- Implement hand evaluation logic for showdown.
- Add persistent storage using a database for player profiles and game history.
- Enhance the user interface and user experience.
- Implement user authentication and leaderboards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the FastAPI community for their excellent documentation and support.
- Inspired by the classic game of Texas Hold'em poker.

---

Feel free to modify any sections to better fit your project's details or add more specific information as needed! Let me know if you need further assistance.