import random as rd

Couleur = ["♠","♥","♦","♣"]
Figure = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
Paquet = []
for i in range(13):
    for j in range(4):
        Paquet.append([Figure[i],Couleur[j]])

def New_paquet():
    New_deck = Paquet[:]
    Deck = []
    while(len(New_deck) >= 1):
        i = rd.randint(0,len(New_deck)-1)
        Deck.append(New_deck[i])
        New_deck.pop(i)
    return Deck

print("Nombre de joueur ?")
nb_player = input()
try:
    int(nb_player)
except:
    print("Le nombre de joueur donné n'est pas un entier...")
    exit()

nb_player = int(nb_player)

if nb_player <= 1 :
    print("Pas assez de joueurs !")
    exit() 

Players = []
for i in range(nb_player):
    print("Joueur n°",i+1,"Pseudo ?")
    string = input()
    Players.append(string)

print("Mise de départ ?")
Start_chip = input()







deck = New_paquet()

print(Paquet)
print('-----------')
print(deck)


