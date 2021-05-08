x = float(input("enter the first intger: "))
y = float(input("enter the second intger: "))


def sum_two(num1, num2):
    total = num1 + num2
    if len(str(total)) >= 80:
        return "Overflow"
    else:
        return total


print(sum_two(x, y))
