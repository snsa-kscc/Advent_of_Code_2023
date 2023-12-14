with open ("day_14/data.txt") as f:
  data = f.read().splitlines()

grid = list(map("".join, zip(*data)))
sorted_grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
transposed_grid = list(map("".join, zip(*sorted_grid)))

total = sum(row.count("O") * (len(transposed_grid) - r) for r, row in enumerate(transposed_grid))

print(total)