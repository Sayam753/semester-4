# Answer 2
def multiply(a, b, bound):
    result = a*b
    if result <= bound:
        return result
    else:
        raise ValueError(
            f'multiplication of {a} and {b} with bound {bound} not possible')


def main(a, b, bound):
    return multiply(a, b, bound)
