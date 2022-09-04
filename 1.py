
def is_valid(password):
    import re
    if re.match(r'^(?=.*[A-Z])(?=.*\d{2})(?=.*[\x00-\x7F])[A-Za-z\d\x00-\x7F]{8,}$', password):
        return True
    else:
        return False


print(is_valid('qwertYa1'))
