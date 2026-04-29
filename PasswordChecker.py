a=input("Enter your password")
up=0
low=0
spec=0
num=0
if len(a) > 7:
    for i in a:
        if i.usupper():
            up=up+1
        elif i.islower():
            low=low+1
        elif i.isdigit():
            num +-1
        else:
            spec=spec+1
    if up>1 and low>1 and spec>1 and num>1:
        print("STRONG")
    else:
        print("weak")
else:
    print("weak password")
    
