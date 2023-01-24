list1=[14,13,-4,45,32,15]
list2=[51,37,-8,5,19,15]
a=len(list1)
b=len(list2)
if(a==b):
 print("same length ")
else:
 print("length is not same")
s1=sum(list1)
s2=sum(list2)
if(s1==s2):
 print("Sum of two list are same")
else:
 print("Sum is different")
print("common elements")
for i in list1:
 for j in list2:
  if(i==j):
   print(i)