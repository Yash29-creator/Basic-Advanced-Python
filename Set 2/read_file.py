f=open('file_read.txt','w')
f1=open('file_read1.txt','r')
data = f1.readline()
f.write(data)
f.close()
f1.close()
with open('file_read.txt', 'r') as f:
    line = f.readline()
    print(f"Line {1}: {line}")

f=open('file_read1.txt', mode='r')
# print(f.read())
line = f.readlines()
print(f"{line}\n{type(line)}")
for i in range(len(line)):
    print(f"Line {i + 1}: {line[i]}")
# n = int(input("Enter number of lines you want to print: "))
# for i in range(n):
#     print(f"Line {i+1}: {line[i]}")
f.close()
