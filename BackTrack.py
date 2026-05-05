def lok(a):
    if a==1:
        return
    a-=1
    lok(a)
    print("Hai")
    lok(a)
lok(5)
