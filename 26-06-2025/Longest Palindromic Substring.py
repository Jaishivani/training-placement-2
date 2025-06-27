def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    start = 0
    max_len = 1
    
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and (j - i + 1) > max_len:
                start = i
                max_len = j - i + 1
    
    return s[start:start+max_len]

# Example usage
text = input("Enter a string: ")
print("Longest Palindromic Substring:", longest_palindrome(text))
