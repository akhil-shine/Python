n=int(input("Enter the number of strings:"))
print("Enter the string:")
list=[]
count=0
for i in range(0,n):
    a=input()
    list.append(a)
print(list)
for i in list:
    for j in i:
        if j=='a':
            count=count+1
print(count)