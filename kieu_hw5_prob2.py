word = "omgthisworks"

print("The original string is : " + word)

i = ""
for idx in range(len(word)):
    if not idx % 2:
        i = i + word[idx].upper()
    else:
        i = i + word[idx].lower()

print("The alterate case string is : " + str(i))