def generate(ind, curr, ans, candidates, target):
    if target == 0:
        ans.append(curr.copy())
        return
    if target < 0 or ind >= len(candidates):
        return

    # Pick the current element
    curr.append(candidates[ind])
    generate(ind + 1, curr, ans, candidates, target - candidates[ind])
    curr.pop()

    # Skip duplicates
    for i in range(ind + 1, len(candidates)):
        if candidates[i] != candidates[ind]:
            generate(i, curr, ans, candidates, target)
            break

def main():
    candidates = list(map(int, input("Enter numbers: ").split()))
    candidates.sort()
    target = int(input("Enter the target: "))
    ans = []
    generate(0, [], ans, candidates, target)
    print("Combinations:", ans)

main()
