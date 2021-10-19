"""
This program will help in generating new random passwords for user for different online accounts.
The user can select the length the number of characters required in the password.
User can select whether to save the password saved to a txt file in the same directory as of this python file.
This program generates password which includes special characters.
"""

from random import shuffle
from random import randint


def rand_pass_list(max_length, character_list, previous_list, last):
    if last:
        pass_list = [character_list[randint(0, len(character_list)-1)] for i in range(0, max_length)]
    else:
        pass_list = [character_list[randint(0, len(character_list)-1)] for i in range(0, (randint(1, max_length)))]
    return pass_list + previous_list


def pass_list_creator(password_length, *args):
    rand_password_list = []
    for i in args:
        index_arg = args.index(i)
        if index_arg == (len(args)-1):
            last = True
        else:
            last = False
        rand_password_list = rand_pass_list(password_length-(3-index_arg)-len(rand_password_list), i,
                                            rand_password_list, last)
    shuffle(rand_password_list)
    return rand_password_list


def password_creator(password_length):
    symbol_list = [symbols for symbols in (' !"#$%&()*+, -./:;<=>?@[\]^_`{|}~' + "'")]
    cap_alpha_list = [letter.upper() for letter in 'abcdefghijklmnopqrstuvwxyz']
    small_alpha_list = [letter.lower() for letter in 'abcdefghijklmnopqrstuvwxyz']
    number_list = [number for number in '0123456789']
    return ''.join(pass_list_creator(password_length,  symbol_list,  cap_alpha_list,  small_alpha_list,  number_list))


def password_length():
    password_length = (input("Default length of password is 15."
                             "\nEnter the length to change or press enter (minimum 4 char): "))
    if password_length == '':
        password_length = 15
    else:
        password_length = int(password_length)
        if password_length < 4:
            password_length = 4
    return password_length


def file_writer():
    new_file = False
    try:
        with open('passwords.txt', mode='r') as p:
            if p.read() == '':
                new_file = True
    except FileNotFoundError:
        new_file = True

    with open('passwords.txt',  mode='a') as p:
        if new_file:
            p.write('{}: {}'.format(name_of_password, password))
            p.close()
        else:
            p.write('\n{}: {}'.format(name_of_password,  password))
            p.close()


name_of_password = input('What is the password for?: ')
password = password_creator(password_length())
print(f'The Password for {name_of_password}: {password}')

while True:
    print_permission = input('Do you want to save the password to the file?(Y/N): ')
    if print_permission.lower() == 'y':
        file_writer()
        break
    elif print_permission.lower() == 'n':
        break
    else:
        print('Invalid Input!!!')
        continue
