import sys

digits = '0123456789'
digit_substitutions = {
    'o': '0', 'i': '1', 'e': '3', 'p': '9', 'a': '4',
    'O': '0', 'I': '1', 'E': '3', 'P': '9', 'A': '4'}

symbols = '^!#$?-@'
symbol_substitutions = {
    'l': '!', 's': '$', 'm': '^^', 'a': '@', 'n': '#',
    'L': '!', 'S': '$', 'M': '^^', 'A': '@', 'N': '#'}

capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitals_substitutions =  {char.lower(): char for char in capitals}

def check_password(password):
    if (contains_character(password, digits) and
        contains_character(password, symbols) and
        contains_character(password, capitals)):
        return True
    else:
        return False

def substitute_password(password):
    n_iter = 0
    while not check_password(password):
        if not contains_character(password, capitals):
            password = substitute_character(password, capitals_substitutions)
        if not contains_character(password, symbols):
            password = substitute_character(password, symbol_substitutions)
        if not contains_character(password, digits):
            password = substitute_character(password, digit_substitutions)
        n_iter = n_iter + 1
        if n_iter > 10:
            raise ValueError("Pick a better password ^^00b!")
            break
    return password

def contains_character(password, characters):
    for char in characters:
        if char in password:
            return True
    return False

def substitute_character(password, substitution_dict):
    for char in password:
        if char in substitution_dict:
            password = password.replace(char, substitution_dict[char])
            break
    return password


password = sys.argv[1]
if check_password(password):
    print("Password is OK!")
else:
    print("Password is BAD!")
    new_password = substitute_password(password)
    print("How about using: ", new_password)
