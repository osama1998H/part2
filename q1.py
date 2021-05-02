# def check(nums: list):
#     for i in nums:
#         for m in nums:
#             if i+1 == m:
#                 break

#                 # print("found double value")


# check([i for i in range(10)])


def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))
