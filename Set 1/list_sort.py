try:
    n = int(input("Enter length of list: "))
    l = []
    for i in range(n):
        a = int(input("Enter number: "))
        l.append(a)
    l.sort()
    rev=l[::-1]
    print(f"Ascending Sort: {l}\nDescending Sort: {rev}")
except ValueError:
    print("Enter proper data.")