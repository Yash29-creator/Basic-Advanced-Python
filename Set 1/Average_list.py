try:
    n = int(input("Enter length of list: "))
    l = []
    for i in range(n):
        a = int(input("Enter number: "))
        l.append(a)
    
    sum_l = 0
    for i in l:
        sum_l += i
    
    avg_l = sum(l)/len(l)
    avg_loop =  sum_l/len(l)
    print(f"Average of list {l} is {avg_l} by sum function and {avg_loop} by loop")
except ValueError:
    print("Enter proper data.")