str=input("Enter the line of text:")
print(str)
dict={}
a=str.split()
print(a)
for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)




