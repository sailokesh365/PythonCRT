a=int(input("Enter the Input: "))
lokesh(a)

def lokesh(a):
    if a==1:
        return
    i=2
    while(a%i != 0):
        i=i+1
    print(i,end=" ")
    lokesh(a/i)
