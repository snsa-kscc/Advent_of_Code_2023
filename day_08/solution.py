with open ("day_08/data.txt") as f:
  steps, _, *rest = f.read().splitlines()

network = {}

for line in rest:
  left, right = line.split(" = ")
  clean_right = right[1:-1].split(", ")
  network[left] = clean_right

step_count = 0
current = 'AAA'

while current != 'ZZZ':
  step_count += 1

  if steps[0] == 'L':
    current = network[current][0]
  else:
    current = network[current][1]
  
  steps = steps[1:] + steps[0]

print(step_count)
