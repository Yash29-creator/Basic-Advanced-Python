def fact(n):
    if n==0: return 1
    else: return n*fact(n-1)

try:
    n = int(input("Enter Number: "))
    print(f"Factorial of {n} is {fact(n)}.")
except ValueError:
    print("Enter proper data.")
