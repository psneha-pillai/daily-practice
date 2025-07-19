def vowels_consonents(s):
    vowels="aeiouAEIOU"
    vowels_count=0
    consonents_count=0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowels_count+=1
            else:
                consonents_count+=1
    print("vowels:",vowels_count)
    print("consonents:",consonents_count)
s=input()
vowels_consonents(s)
