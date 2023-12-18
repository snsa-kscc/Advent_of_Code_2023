with open("day_18/data.txt") as f:
  data = f.read().splitlines()

points = [(0, 0)]
dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

b = 0

for line in data:
  d, n, _ = line.split()
  dr, dc = dirs[d]
  n = int(n)
  b += n
  r, c = points[-1]
  points.append((r + n * dr, c + n * dc))

A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i +1) % len(points)][1]) for i in range(len(points)))) // 2
i = A - b // 2 + 1

print(i + b)
