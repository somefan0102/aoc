import sys

B = len(sys.argv) > 1 and sys.argv[1] == "b"
*lines, ops = sys.stdin.readlines()
result = 0

fold = lambda l, i, f: None if i > len(l)-1 else f(l[i], fold(l, i+1, f))
add  = lambda a, b: a + b if b else a + 0
mult = lambda a, b: a * b if b else a * 1

cols = [[]]

if B:
    i = 0
    while i < max(map(lambda l: len(l), lines)):
        col = "".join(map(lambda l: l[i], lines))
        if col.isspace():
            cols.append([])
        else:
            cols[-1].append(int(col))
        i += 1
    cols.pop()
    
    for col, op in zip(reversed(cols), reversed(ops.split())):
        result += fold(col, 0, add if op == "+" else mult)
else:
    lines = map(lambda l: list(map(int, l.split())), lines)
    for lines, op in zip(zip(*lines), ops.split()):
        result += fold(lines, 0, add if op == "+" else mult)

print(result)