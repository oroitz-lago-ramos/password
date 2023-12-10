import string
def password_verification(password):
    is_upper = False
    is_lower = False
    is_digit = False
    is_special = False 
    if len(password) < 8:
        return False
    for i in password:
        if i.islower():
            is_lower = True
        elif i.isupper():
            is_upper = True
        elif i.isdigit():
            is_digit = True
        elif i in string.punctuation:
            is_special = True
    if  not is_upper or not is_lower or not is_digit or not is_special:
        return False
    return True