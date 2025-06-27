def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: remove spaces
    return s == s[::-1]

# Example usage
text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
