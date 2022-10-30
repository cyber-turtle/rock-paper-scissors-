import random
import time


def play():
    user = input('[R] for rock [P] for paper [S] for scissors: ').upper()
    computer_choice = random.choice(['R', 'P', 'S'])
    # instance for draw

    if user == computer_choice:
        print(f'you chose {user} and computer chose {computer_choice}')
        print('it\'s a draw!')
    # every other instance
    elif user == 'R' and computer_choice == 'P':
        print(f'you chose {user} and computer chose {computer_choice}')
        print('paper covers rock silly')
        time.sleep(1)
        print('you thought you were THE ROCK did\'nt you.......')

        print('COMPUTER WINS')
    elif user == 'R' and computer_choice == 'S':
        print(f'you chose {user} and computer chose {computer_choice}')
        print('.....')
        time.sleep(1)
        print('SC1SSOR.exe stopped working')
        time.sleep(1)
        print('rock smashes scissors')

        print('USER WINS')
    elif user == 'P' and computer_choice == 'R':
        print(f'you chose {user} and computer chose {computer_choice}')
        print('I win this time around!')
        time.sleep(1)
        print('+1 points for humanity')

        print('USER WINS')
    elif user == 'P' and computer_choice == 'S':
        print(f'you chose {user} and computer chose {computer_choice}')
        print('Sp1C3y dice')
        time.sleep(1)
        print('you got shred to bits!')

        print('COMPUTER WINS')
    elif user == 'S' and computer_choice == 'P':
        print(f'you chose {user} and computer chose {computer_choice}')
        print('hmmm')
        time.sleep(1)
        print('diced meat')
        time.sleep(1)
        print('......')

        print('USER WINS')
    elif user == 'S' and computer_choice == 'R':
        print(f'you chose {user} and computer chose {computer_choice}')
        print('I\'m as strong as a boulder are\'nt i?.......')
        time.sleep(1)
        print('well, K.O')
        time.sleep(1)
        print('F A T A L I T Y')

        print('COMPUTER WINS')
    else:
        print('i dont understand, pick between [R] [P] [S]')


play()
