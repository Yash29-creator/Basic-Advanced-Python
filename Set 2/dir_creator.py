import os

print(f"The current working directory is : {os.getcwd()}")
if not os.path.isdir(os.path.join(os.getcwd(),'Data')):
    os.mkdir('Data')
else:
    print("Folder exist")

dir_list = [d for d in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), d))]
print(f"Sub-directories are: {dir_list}")