import sys

B = len(sys.argv) > 1 and sys.argv[1] == "b"
NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
grid = sys.stdin.readlines()
total = 0
done = False

while not done:
    prev = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@': continue
            count = 0
            for n in NEIGHBORS:
                n_i, n_j = i+n[0], j+n[1]
                if n_i < 0 or  n_j < 0 or n_i > len(grid[i])-1 or n_j > len(grid[j])-1: continue
                if grid[n_i][n_j] == '@':
                    count += 1
            if count < 4:
                prev[i] = prev[i][:j] + "." + prev[i][j+1:]
                total += 1
    done = grid == prev if B else True
    grid = prev.copy()

print(total)