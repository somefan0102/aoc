import sys

B = len(sys.argv) > 1 and sys.argv[1] == "b"
p = 50
zeroes = 0

for line in sys.stdin.readlines():
    rot, dist = line[0], int(line[1:])
    for i in range(dist):
        p += (-1 if rot == "L" else 1)
        p %= 100
        if p == 0 and ((i == dist-1 and not B) or B):
            zeroes += 1

print(zeroes)