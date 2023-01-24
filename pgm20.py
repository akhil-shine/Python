a=int(input("Enter the limit:"))
f1=0
f2=1
print("fibonacci series:")
i=3
while(i<=a):
    next=f1+f2
    print(next)
    f1=f2
    f2=next
    i += 1