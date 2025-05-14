'''types of tree'''
'''unique value in the list[1 1 2 2 3]'''
'''prime number ,count vowels in the string'''

n = int(input("Enter a number: "))
if n <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
        break
    if is_prime:
        print("Prime")
    else:
        print("Not prime")
