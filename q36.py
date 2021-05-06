n = float(input("enter the intrest: "))
mounths = int(input("enter the mounths number: "))
dept = float(input("enter the dept: "))


def newmethod792(n, dept, mounths: int):
    n = n / 100

    intrest_value = (dept * n) * mounths

    total_dept = dept + intrest_value
    return f"{round(total_dept, 1)} $"


print(newmethod792(n, dept, mounths))
