from os import system, name


def clear_screen():
    # For Windows
    if name == 'nt':
        system('cls')
    # For mac and linux(here, os.name is 'posix')
    elif name == 'posix':
        system('clear')


def user_name():
    clear_screen()
    user_1 = input('Name of Player 1: ')
    user_2 = input('Name of Player 2: ')
    return [user_1, user_2]


def choose_symbol(user_names):
    clear_screen()
    user1_symb = 'empty'
    user2_symb = 'empty'
    while True:
        user1_symb_choice = input(f'X or O for {user_names[0]}: ')
        if user1_symb_choice.lower() == 'x':
            user1_symb = 'X'
            user2_symb = 'O'
            break
        elif user1_symb_choice.lower() == 'o' or user1_symb_choice == '0':
            user1_symb = 'O'
            user2_symb = 'X'
            break
        else:
            print('Invalid Input!')
            continue
    return {user_names[0]: user1_symb, user_names[1]: user2_symb}


def display_game(pos_list, user_details, user_names):
    clear_screen()
    print('*********************')
    print('TIC TAC TOE')
    print('*********************')
    for user in user_names:
        print(f'{user}: {user_details[user]}')
    game = ''
    blank_line = '   |   |   '
    horizontal_lines = '-----------'
    game = game + blank_line + '\n' + f' {pos_list[0]} | {pos_list[1]} | {pos_list[2]} ' + '\n' + blank_line + '\n' + horizontal_lines + '\n'
    game = game + blank_line + '\n' + f' {pos_list[3]} | {pos_list[4]} | {pos_list[5]} ' + '\n' + blank_line + '\n' + horizontal_lines + '\n'
    game = game + blank_line + '\n' + f' {pos_list[6]} | {pos_list[7]} | {pos_list[8]} ' + '\n' + blank_line
    print('\n' + game + '\n')


def position_input_verify(user, pos_list):
    while True:
        pos_str = (input(f'"{user}" - enter the position to mark: '))
        if pos_str in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            pos = int(pos_str)
        else:
            print('Invalid Input!!!')
            continue
        if pos_list[pos-1] == 'X' or pos_list[pos-1] == 'O':
            print('Already filled, Try Another position')
            continue
        else:
            break
    return pos


def position_editor(user, user_details, pos_list):
    pos = position_input_verify(user, pos_list)
    pos_list[pos-1] = user_details[user]
    return pos_list


def win_draw(pos_list, user):
    # For horizontal combinations:
    for x in range(0, 7, 3):
        if pos_list[x] == pos_list[x+1] == pos_list[x+2]:
            print(f'CONGRATULATIONS!!! {user} WON THE GAME')
            return True
    # For vertical combinations:
    for x in range(0, 3):
        if pos_list[x] == pos_list[x + 3] == pos_list[x + 6]:
            print(f'CONGRATULATIONS!!! {user} WON THE GAME')
            return True
    # For cross combinations:
    if pos_list[0] == pos_list[4] == pos_list[8] or pos_list[2] == pos_list[4] == pos_list[6]:
        print(f'CONGRATULATIONS!!! {user} WON THE GAME')
        return True
    # To check draw:
    for x in range(0, 9):
        if pos_list[x] in range(1, 10):
            return False
    print('Draw Match ;)')
    return True


def continue_game():
    while True:
        to_cont = input("Do you want to play again? (Y/N): ").lower()
        if to_cont.lower() == 'y' or to_cont.lower() == 'n':
            if to_cont.lower() == 'y':
                return True
            else:
                return False
        print('Invalid Input!!!')


while True:
    user_names = user_name()
    user_details = choose_symbol(user_names)
    pos_list = list(range(1, 10))
    display_game(pos_list, user_details, user_names)
    game_continue = None
    while True:
        for user in user_names:
            pos_list = position_editor(user, user_details, pos_list)
            display_game(pos_list, user_details, user_names)
            stop_game = win_draw(pos_list, user)
            if stop_game is True:
                break
        if stop_game is True:
            break
        else:
            continue
    if continue_game() is True:
        continue
    else:
        print('Thank You for Playing The Game')
        break
