for i in range(1000,10000):
    for j in range(32,100):
        if i==j*j:
            string=str(i)
            if int(string[0])%2==0 and int(string[1])%2==0 and int(string[2])%2==0 and int(string[3])%2==0:
                print(i)