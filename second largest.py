def second_largest(n):
    if len(n) < 2:
        return "List must contain at least two elements"

    largest = second = float("-inf")

    for num in n:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float("-inf"):
        return "No second largest element, all elements may be the same"
    else:
        return second

# Input
n = list(map(int, input("Enter numbers separated by space: ").split()))
print(second_largest(n))
