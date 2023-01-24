n = int(input("Enter the limit: "))
x = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        x = i*j
        print(x, end=" ")
    print()
