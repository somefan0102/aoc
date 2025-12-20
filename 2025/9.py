import sys

grid = []
coors = []

for coor in sys.stdin.readlines():
    coors.append(list(map(int, coor.split(","))))

largest_coords = None
largest_area = 0

for coor1 in coors:
    for coor2 in coors:
        if coor1 == coor2: continue
        x1, y1 = coor1
        x2, y2 = coor2
        area = (max(x1, x2)-min(x1, x2)+1) * (max(y1, y2)-min(y1, y2)+1)

        if area > largest_area:
            largest_coords = [coor1, coor2]
            largest_area = area

print(largest_area)