n = int(input())

# Upper half of the diamond
for i in range(0, n):
    for j in range(n - i - 1):
        print(" ", end="")  # Print space
    for j in range(2 * i + 1):
        print("*", end="")  # Print star
    print()

# Lower half of the diamond
for i in range(0, n):
    for j in range(i):
        print(" ", end="")  # Print space
    for j in range(2 * (n - i) - 1):
        print("*", end="")  # Print star
    print()
