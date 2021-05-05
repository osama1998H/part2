height_list = input("Enter Th Height Numbers List Sepratie With Space:  ")
print("\n")
print("----------------------------------------------|")
print("\n")


def new_func(height_list):
    height_list = height_list.split()
    print(height_list, "\n")
    data = [int(i) for i in height_list]
    data = sorted(data)
    print(f"The 1st Heigest Building Is: {data[-1]}\n")
    print(f"The 2se Heigest Building Is: {data[-2]}\n")
    print(f"The 3th Heigest Building Is: {data[-3]}\n")


new_func(height_list)
