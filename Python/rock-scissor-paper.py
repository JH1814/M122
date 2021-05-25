# STEIN, SCHERE, PAPIER
# Dieser Code implementiert eine Version des Spiels, bei dem Sie
# gegen den Computer spielen.
# Hier bereiten wir das Programm vor, indem wir das random-Modul
# importieren und die Variable winner definieren.

import random
winner = ''

# Der Computer wählt zufällig Stein (rock), Schere (scissors)
# oder Papier (paper), indem er eine Zufallszahl zwischen 0 und 2 # erzeugt und diese auf den passenden String abbildet.


computer_pt = 0
spieler_pt = 0


def spielen():

    random_choice = random.randint(0, 2)
    print(random_choice)
    if random_choice == 0:
        computer_choice = 'rock'
    elif random_choice == 1:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'

    # Die Wahl des Benutzers mit einer einfachen input-Anweisung ermitteln.
    user_choice = input('rock, paper or scissors? ')
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        # Dies ist die Spiellogik, die überprüft, ob der Computer gewinnt
        # (oder nicht), und die nötigen Änderungen an der winner-Variablen vornimmt.
        if computer_choice == user_choice:
            winner = 'Tie'
        elif (computer_choice == 'paper' and user_choice == 'rock' or computer_choice == 'rock' and user_choice == 'scissors' or computer_choice == 'scissors' and user_choice == 'paper'):
            winner = 'Computer'
        


        else:
            winner = 'User'

        # Hier geben wir aus, ob das Spiel unentschieden war.
        # Falls nicht, verkünden wir den Gewinner und die Wahl des Computers.
        if winner == 'Tie':
            print('We both chose', computer_choice + ', play again.')
        else:
            print(winner, 'won. The computer chose', computer_choice + '.')

        return winner
        
    else:
        print("invalid input, try again")
        spielen()


while computer_pt < 3 and spieler_pt < 3:
    print(str(computer_pt) + "< 3  or  "+str(spieler_pt) + " < 3")
    thewinner = spielen()
    if thewinner == 'computer':
        computer_pt += 1
    elif thewinner == 'User':
        spieler_pt += 1
