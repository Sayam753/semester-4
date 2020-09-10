# Question 1
def even(start, n):
    if start % 2 == 1:
        start = start+1
    return [n for n in range(start, start+2*n-1, 2)]


def main(start, n):
    return even(start, n)
