def longestLength(a):
    length = len(s[0])
    word = s[0]
    for i in a:
        if (len(i) > length):
            length = len(i)
            word = i
    print("The longest word is ", word,
          " and its length is ", length)
n=int(input("Enter the size: "))
print("Enter the elements: ")
s=[]
for i in range(0,n):
    ele=input()
    s.append(ele)
print("S=",s)
longestLength(s)