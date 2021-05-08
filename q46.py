import datetime

d, m = map(int, input("Enter The Date D M:").split())

print(d, m)

data = datetime.datetime(2021, m, d)

week = {
    0: "mon",
    1: "tus",
    2: "wed",
    3: "thr",
    4: "fri",
    5: "sat",
}
print(week[data.weekday()])


