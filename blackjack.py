from random import randint

# on initialie le jeu de carte
cards = [
    '2 de trèfle',
    '2 de carreau',
    '2 de pique',
    '2 de coeur',
    '3 de trèfle',
    '3 de carreau',
    '3 de pique',
    '3 de coeur',
    '4 de trèfle',
    '4 de carreau',
    '4 de pique',
    '4 de coeur',
    '5 de trèfle',
    '5 de carreau',
    '5 de pique',
    '5 de coeur',
    '6 de trèfle',
    '6 de carreau',
    '6 de pique',
    '6 de coeur',
    '7 de trèfle',
    '7 de carreau',
    '7 de pique',
    '7 de coeur',
    '8 de trèfle',
    '8 de carreau',
    '8 de pique',
    '8 de coeur',
    '9 de trèfle',
    '9 de carreau',
    '9 de pique',
    '9 de coeur',
    '10 de trèfle',
    '10 de carreau',
    '10 de pique',
    '10 de coeur',
    'valet de trèfle',
    'valet de carreau',
    'valet de pique',
    'valet de coeur',
    'dame de trèfle',
    'dame de carreau',
    'dame de pique',
    'dame de coeur',
    'roi de trèfle',
    'roi de carreau',
    'roi de pique',
    'roi de coeur',
    'as de trèfle',
    'as de carreau',
    'as de pique',
    'as de coeur',
]
# liste des cartes du joueur et de la banque
joueur = []
bank = []

# permet de dire si le joueur reprends une carte ou garde ses cartes
reste = False

# permet de compter les valeurs des cartes du joueur (values[0]) et de la banque (values[1])
values = [0, 0]

# permet de compter la valeur de la dernière carte pioché
j = 1
k = 1

print('La banque bats les cartes.')

# on mélange les cartes de manière aléatoire
for i in range(0, len(cards)):
    indice1 = randint(0, len(cards) - 1)
    indice2 = randint(0, len(cards) - 1)
    a = cards[indice1]
    cards[indice1] = cards[indice2]
    cards[indice2] = cards[indice1]

print('La banque distribue au joueur et à elle-même une carte.')
joueur.append(cards[0])
cards.remove(cards[0])

bank.append(cards[0])
cards.remove(cards[0])

print('Vos cartes : ', joueur)

# on calcul la valeur de la carte du joueur et de la banque
try:
    numbers = int(joueur[0].split("de")[0])
    values[0] += numbers
except:
    if joueur[0][0] == 'a' and joueur[0][1] == 's':
        values[0] += 11
    else:
        values[0] += 10

try:
    numbers = int(bank[0].split("de")[0])
    values[1] += numbers
except:
    if bank[0][0] == 'a' and bank[0][1] == 's':
        values[1] += 11
    else:
        values[1] += 10

while reste == False:
    answer = input('Voulez-vous une nouvelle carte ? (oui ou non) : ')
    if answer.lower() == 'oui':
        print('Carte !')
        joueur.append(cards[0])
        cards.remove(cards[0])

        # on calcul à chaque tirage la somme des valeurs des cartes
        try:
            numbers = int(joueur[j].split("de")[0])
            values[0] += numbers
        except:
            if joueur[j][0] == 'a' and joueur[j][1] == 's':
                values[0] += 11
            else:
                values[0] += 10
        j += 1

        print("Vos cartes : ", joueur)
    elif answer.lower() == 'non':
        print('Je reste !')
        reste = True
    else:
        print('Veuillez répondre par oui ou non.')

print("Le joueur a atteint %i." % (values[0]))

if values[0] == 21:
    print("Le joueur a gagné !")
elif values[0] > 21:
    print("Le joueur a perdu !")
else:
    print("La banque tire des cartes.")
    while values[1] <= values[0]:
        bank.append(cards[0])
        cards.remove(cards[0])

        # on calcul à chaque tirage de la banque la somme de valeurs des cartes
        try:
            numbers = int(bank[k].split("de")[0])
            values[1] += numbers
        except:
            if bank[k][0] == 'a' and bank[k][1] == 's':
                values[1] += 11
            else:
                values[1] += 10
        k += 1

    if values[1] > values[0] and values[1] < 21:
        print("La banque a atteint %i, la banque a gagné !" % (values[1]))
    elif values[1] > 21:
        print("La banque a atteint %i, la banque a perdu, le joueur gagne !" % (values[1]))