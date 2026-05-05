import random

a = int(input("Enter no of teams : "))
teams = []

print("Enter all teams names : ")

for i in range(a):
    t = input("Enter team name : ")
    teams.append(t)
m=int(input("Enter num of meet bw teams : "))

matches = []
for i in range(0,a-1):
    for j in range(i+1,a):
        for k in range(m):
            matches.append([teams[i],teams[j]])
pos = 1
random.shuffle(matches)
for i in matches:
    print("MATCH {} : {} vs {}".format(pos,i[0],i[1]))
    pos = pos + 1
