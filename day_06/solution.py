with open('day_06/data.txt', 'r') as f:
  data = f.read().splitlines()

times, distances = [list(map(int, line.split(':')[1].split())) for line in data]

total_1 = 1

for time, distance in zip(times, distances):
  counter = 0
  for hold in range(time):
    if hold * (time - hold) > distance:
      counter += 1
  total_1 *= counter

print(total_1)

singleton_time, singleton_distance = [list(map(int, ["".join(line.split(':')[1].split())])) for line in data]

total_2 = 1

for time, distance in zip(singleton_time, singleton_distance):
  counter = 0
  for hold in range(time):
    if hold * (time - hold) > distance:
      counter += 1
  total_2 *= counter

print(total_2)