import string
import random

only_num = string.digits
only_letter = string.ascii_letters
num_letter = string.digits+string.ascii_letters
num_sym = string.digits+string.punctuation
letter_sym = string.ascii_letters+string.punctuation
all_comb = string.ascii_letters+string.digits+string.punctuation

try:
    n = int(input("Enter length: "))
    if n<=0:
        raise ValueError("Enter positive integer.")
    print("Enter 1 for alphabets only.\nEnter 2 for digits only.")
    print("Enter 3 for alphabets and digits.\nEnter 4 for all combinations.")
    print("Enter any other number for exit.\nBy default criteria is combination of all.")
    comb = int(input("Enter choice: "))
    if comb==1:
        password = ''.join(random.choice(only_letter) for i in range(n))
    elif comb==2:
        password = ''.join(random.choice(only_num) for i in range(n))
    elif comb==3:
        password = ''.join(random.choice(num_letter) for i in range(n))
    elif comb==4:
        password = ''.join(random.choice(all_comb) for i in range(n))
    else:
        password = ''.join(random.choice(all_comb) for i in range(n))
    print(f"Your password for length of {n} is {password}")
except ValueError:
    print("Enter proper data.")