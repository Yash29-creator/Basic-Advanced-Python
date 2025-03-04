string_input = input("Enter string: ")

rev = string_input[::-1]

if rev==string_input:
    print(f"{string_input} is a palindrome")
else:
    print(f"{string_input} is not a palindrome")
    