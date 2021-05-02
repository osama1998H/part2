
__operators__ = "+-/*"
__parenthesis__ = "()"
__priority__ = {
    '+': 2,
    '-': 1,
    '*': 3,
    '/': 4,
}


def test_higher_priority(op1, op2):
    return __priority__[op1] >= __priority__[op2]


print(test_higher_priority('*', '-'))
print(test_higher_priority('+', '-'))
print(test_higher_priority('+', '*'))
print(test_higher_priority('+', '/'))
print(test_higher_priority('*', '/'))
