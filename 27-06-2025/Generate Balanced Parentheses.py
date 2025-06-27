def generate_parens(open, close, s, n):
    if len(s) == 2 * n:
        print(s)
        return
    if open < n:
        generate_parens(open + 1, close, s + "(", n)
    if close < open:
        generate_parens(open, close + 1, s + ")", n)

n = int(input("Enter number of pairs: "))
generate_parens(0, 0, "", n)
