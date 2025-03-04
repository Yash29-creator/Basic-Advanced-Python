try:
    n = int(input("Enter number: "))
    for i in range(1,11):
        print(f"{n} × {i} = {n*i}")
    
except ValueError:
    print("Enter proper data.")