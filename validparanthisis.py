class Solution:
    def isValid(self, s: str) -> bool:
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""

# Take input from the user
user_input = input("Enter a bracket string (e.g., ()[]{}): ")

# Create Solution instance
sol = Solution()

# Validate input
if sol.isValid(user_input):
    print("Valid parentheses!")
else:
    print("Invalid parentheses.")
