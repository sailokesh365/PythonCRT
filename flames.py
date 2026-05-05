name1 = input("Enter first name: ").lower().replace(" ", "")
name2 = input("Enter second name: ").lower().replace(" ", "")
for i in name1:
    if i in name2:
        name1 = name1.replace(i, '', 1)
        name2 = name2.replace(i, '', 1)

count = len(name1) + len(name2)
flames = ["F", "L", "A", "M", "E", "S"]
while len(flames) > 1:
    index = (count % len(flames)) - 1

    if index >= 0:
        flames = flames[index+1:] + flames[:index]
    else:
        flames.pop()
result = {
    "F": "Friends", "L": "Love","A": "Affection","M": "Marriage","E": "Enemies","S": "Siblings"
}
print("Relationship:", result[flames[0]])
