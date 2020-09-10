# Question 10
def countPatterns(n):
    # Write your code here
    mod = 10**9 + 7
    ans = ((24**n) % mod - (9*(8**n)) % mod + (18*(3**n)) %
           mod + (9*(2**n)) % mod - 24) % mod
    return ans


def main(n):
    return countPatterns(n)
