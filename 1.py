import re


def is_valid(password):
    if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d{2})(?=.*[\x00-\x7F])[A-Za-z\d\x00-\x7F]{8,}$', password):
        print(True)
    else:
        print(False)


is_valid('Qwerty1234')