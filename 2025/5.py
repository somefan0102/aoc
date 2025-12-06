import sys

B = len(sys.argv) > 1 and sys.argv[1] == "b"
split = lambda x: x.split()
ranges, samples = map(split, sys.stdin.read().split("\n\n"))
numbers = []

for r in ranges:
    x, y = map(int, r.split("-"))
    numbers.append((x, y))
numbers = sorted(numbers)

if B:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if j == i or numbers[i] == None or numbers[j] == None:
                continue

            a, b, c, d = numbers[i] + numbers[j]

            if b >= c:
                new = (min(a, b, c, d), max(a, b, c, d))
                numbers[i] = new
                numbers[j] = None

    diff = lambda l: 0 if l == None else l[1] - l[0] + 1
    print(sum(map(diff, numbers)))
else:
    count = 0

    for sample in samples:
        for n in numbers:
            if n[0] <= int(sample) <= n[1]:
                count += 1
                break

    print(count)