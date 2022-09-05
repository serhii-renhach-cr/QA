
def is_valid(password):
    import re
    if re.match(r'^(?=.*[A-Z])(?=.*\d{2})(?=.*[\x00-\x7F])[A-Za-z\d\x00-\x7F]{8,}$', password):
        return True
    else:
        return False


print(is_valid('Qwerty1234'))
print(is_valid('QWERTY1234'))
print(is_valid('12345678'))
print(is_valid('qwertyqwerty'))
print(is_valid('qwerty12'))
print(is_valid('Qwertyq1'))
print(is_valid('QWERTYQWERTY'))
print(is_valid('Qwerty  1234'))
print(is_valid('Qwerty1234#$%'))
print(is_valid('        qw12Q'))
print(is_valid('@#$%^&*@Q12'))
