import sys

B = len(sys.argv) > 1 and sys.argv[1] == "b"
invalids = []

for scope in sys.stdin.readline().split(","):
    x, y = scope.split("-")

    for i in range(int(x), int(y)+1):
        i = str(i)

        for j in range(1, len(i)):
            by = len(i)/j

            if by % 1 != 0 or (len(invalids) and str(invalids[-1]) == i) or ((not B) and by != 2):
                continue

            if i == i[0:j] * int(by):
                invalids.append(int(i))

print(sum(invalids))