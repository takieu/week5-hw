def isPalindrome(i):
    return i == i[::-1]

i = input("Enter word: ")

answer = isPalindrome(i)

if answer:
    print("Yes")
else:
    print("No")