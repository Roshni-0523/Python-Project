def prime(low,high):
    if (low<=1):
        low=2
    c,d=0,0
    for i in range(low,high+1):
        m=0
        for j in range(1,i+1):
            if i%j==0:
                m=m+1
        if m==2:
            print("Prime=",i)
            c+=1
        else:
            print("Composite=",i)
            d+=1
    print("number of prime numbers=",c)
    print("number of composite numbers=",d)
low=int(input('Lower Limit: '))
high=int(input('Higher Limit:'))
prime(low,high)