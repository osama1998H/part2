data = list(map(int, input("enter x1,y1,x2,y2,x3,y3,x4,y4: valuse: ").split()))
x1, y1, x2, y2, x3, y3, x4, y4 = data

# print(x1,y1,x2,y2,x3,y3,x4,y4)

pq = [[x1, y1], [x2, y2]]
rs = [[x3, y3], [x4, y4]]
# print(pq[0][1], rs)


def slope(point: list):
    up = point[1][1] - point[0][1]
    down = point[1][0] - point[0][0]
    if down == 0:
        return "inf"
    else:
        mid = up / down
        return mid


if round(slope(pq)) == round(slope(rs)):
    print("lines are parallel")
else:
    print("not parallel")
