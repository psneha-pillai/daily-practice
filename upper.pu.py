n=input("enter a string:")
result=""
for char in n:
    if char in "aeiou":
        result+= char(ord(char)-32)
    elif char in n:
        result+=char(ord(char)+32)
    else:
        result+=char
print(result)
