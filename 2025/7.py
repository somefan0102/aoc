import sys

lines = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))
times = 0

lines[1]["".join(lines[0]).find("S")] = "|"

for i in range(1, len(lines)-1):
  for j in range(len(lines[i])):
      if lines[i][j] == '|':
        if lines[i+1][j] == '^':
          lines[i+1][j-1] = '|'
          lines[i+1][j+1] = '|'
          times += 1
        else:
          lines[i+1][j] = '|'

print(timelines)