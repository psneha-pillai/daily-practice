#without isalpha
def vowels_consonents(s):
    vowels="aeiouAEIOU"
    vowels_count=0
    consonent_count=0
    for char in s:
        if ("A"<=char<="Z") or ("a"<=char<="z"):
            if char in vowels:
                vowels_count+=1
            else:
                consonent_count+=1
    print("vowels:",vowels_count)
    print("consonent:",consonent_count)
s=input()
vowels_consonents(s)
