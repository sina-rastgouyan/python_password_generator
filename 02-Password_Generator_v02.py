import random
import string
import os

settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
}

def cleaned_screen():
    return os.system('cls')


def get_yes_no_settings(option, default):
    while True:
        user_input = input(
            f"include {option}? default: {default}"
            "(y: yes, n: no, enter: default)\n").lower()
        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'

        print("Invalid Input.Please Try Again.")


def get_user_password_length(opiton, default):
    while True:
        user_input = input(
            "Please Enter A Number To Set Length For Password:"
            f"default length: {default}(enter: default)\n")

        if user_input == '':
            return default

        if user_input.isdigit():
            user_password_length = int(user_input)
            if 6 <= user_password_length <= 30:
                return user_password_length
            print("Password length should be between 6 and 30.")
        else:
            print("Invalid input. You should enter a number")
        print("Try Again!")


def get_settings_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_no_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length


def lower_case_container():
    return string.ascii_lowercase

def upper_case_container():
    return string.ascii_uppercase

def symol_chars_container():
    return string.punctuation

def numbers_container():
    return string.digits


def get_random_char(user_checked_settings):
    get_random_checked = random.choice(user_checked_settings)
    if get_random_checked == 'lower':
        return random.choice(lower_case_container())
    if get_random_checked == 'upper':
        return random.choice(upper_case_container())
    if get_random_checked == 'symbol':
        return random.choice(symol_chars_container())
    if get_random_checked == 'number':
        return random.choice(numbers_container())
    if get_random_checked == 'space':
        return ' '
def password_generator(settings):
    password = ''
    user_checked_settings = list(filter(lambda checked: settings[checked],
                                        ['lower', 'upper', 'symbol', 'number', 'space']))

    for i in range(settings['length']):
        password += get_random_char(user_checked_settings)
    return password

def regenerate_password():
    while True:
        user_decision = input("Do you want to regenerate password: (y/enter: yes    n: no)").lower()
        if user_decision in ['y', 'n', '']:
            if user_decision == 'n':
                return user_decision
            break
        else:
            print('Invalid input. Please Choose From (y/enter: yes    n: no)')


def password_generator_loop():
    while True:
        print('-' * 24)
        print("Generated Password:\n")
        print(password_generator(settings))
        user_decision = regenerate_password()
        if user_decision == 'n':
            return


def run_program():
    cleaned_screen()
    get_settings_from_user(settings)
    password_generator_loop()



run_program()