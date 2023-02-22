import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')

    user_option = input('piedra, papel o tijera =>')
    user_option = user_option.lower()

    if not user_option in options:
        print('Esa opción no es válida')
        return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User ganó!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Computer ganó!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('User ganó!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('Computer ganó!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('User ganó!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Computer ganó!')
            computer_wins += 1
    
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    result = False
    if computer_wins == 2:
        print('El ganador es la computadora')
        result = True

    if user_wins == 2:
        print('El ganador es el usuario')
        result = True

    return result

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_winds', computer_wins)
        print('user_wins', user_wins)

        rounds += 1

        user_option, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if check_winner(user_wins, computer_wins) == True:
            break

run_game()