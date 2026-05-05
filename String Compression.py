x="AAAACCCDDAAD"
res=""
c=0
for i in range(len(x)):
    if i+1 < len(x) and x[i]==x[i+1]:
        c=c+1
    else:
        res=res+x[i]
        res=res+str(c)
        c=1
print(res)
