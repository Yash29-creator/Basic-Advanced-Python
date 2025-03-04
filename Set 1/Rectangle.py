def area():
    try:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        a = l*b
        print(f"Area of rectangle with length {l} unit and breadth {b} unit is {a} unit sq.")
    except ValueError:
        print("Enter proper data")

def peri():
    try:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        p = 2*(l+b)
        print(f"Perimeter of rectangle with length {l} unit and breadth {b} unit is {p} unit")
    except ValueError:
        print("Enter proper data")

print("Enter 1 for calculating Area.\nEnter 2 for calculating Perimeter.\nEnter any other number for exit")

while True:
    try:
        a = int(input("Enter choice: "))
        if a==1:
            area()
        elif a==2:
            peri()
        else:
            break
    except ValueError:
        print("Enter proper choice.")
