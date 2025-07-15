import random
from string import ascii_letters

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', "@"]


def pass_generator():
    pass_A = []
    nr_A = int(input("How many letters?\n"))
    for i in range(0, nr_A):
        pass_A += random.choice(ascii_letters)

    pass_B = []
    nr_B = int(input("How many numbers?\n"))
    for i in range(0, nr_B):
        pass_B += random.choice(numbers)
        
    pass_C = []
    nr_C = int(input("How many characters?\n"))
    for i in range(0, nr_C):
        pass_C += random.choice(symbols)
    psswrd = pass_A + pass_B + pass_C
        
    password = ""
    random.shuffle(psswrd)
    for z in psswrd:
        password += z
    print(f"Password is {password}\n")
    
pass_generator()
