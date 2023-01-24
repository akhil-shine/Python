n=int(input("Enter the elements:"))
print("Enter the elements:")
list=[]
for i in range(0,n):
    i=int(input())
    if (i>100):
     list.append("over")
    else:
        list.append(i)
print(list)