n=int(input("enter the size of list:"))
print("enter the elements")
l=[]
l2=[]
for i in range (0,n):
    ele = int(input())
    l.append(ele)
    if ele%2!=0:
        l2.append(ele)
print(l)
print(l2)