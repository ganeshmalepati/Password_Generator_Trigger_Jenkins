import random

def password_generator(n_letters, n_numbers, n_symbols):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "$@#&*!"
    password = random.choices(letters, k = n_letters) + random.choices(numbers, k = n_numbers) + random.choices(symbols, k = n_symbols)
    random.shuffle(password)
    Generated_Password = ''.join(password)
    return Generated_Password

n_letters = 6
n_numbers = 3
n_symbols = 1
a = password_generator(n_letters, n_numbers, n_symbols)
print("The Generated Password is: {}".format(a))

    
