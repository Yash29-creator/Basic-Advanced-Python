
def leap_Year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

try:
    n = int(input("Enter year: "))
    if n<=0:
        raise ValueError("Please enter proper year.")
    leap_Year(n)
except ValueError:
    print("Enter proper data.")