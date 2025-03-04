# Aim
# Problem statement
# Algo
# Source code
# Expected o/p

def cel_2_fah():
    try:
        c = float(input("Enter temperature in Celsius "))
        f = ((9*c)/5)+32
        print(f"{c} degree celsius is equivalent to {f} degree fahrenheit")
    except ValueError:
        print("Enter proper data. ￣へ￣")

def fah_2_cel():
    try:
        f = float(input("Enter temperature in Fahrenheit "))
        c = ((f-32)*5)/9
        print(f"{f} degree fahrenheit is equivalent to {c} degree celsius")
    except ValueError:
        print("Enter proper data. ￣へ￣")

print("Enter 1 for Celsius to Fahrenheit")
print("Enter 1 for Fahrenheit to Celsius")

while True:
    try:
        a = int(input("Enter choice: "))
        if a==1:
            cel_2_fah()
        elif a==2:
            fah_2_cel()
        else:
            break
    except ValueError:
        print("Enter Proper Choice. ￣へ￣")
