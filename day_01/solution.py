data_file = "day_01/data.txt"

with open(data_file, "r") as f:
  data = f.read().splitlines()

values = []

for line in data:
  first_number_char = next((char for char in line if char.isdigit()), None)
  last_number_char = next((char for char in reversed(line) if char.isdigit()), None)
  two_digit_char = first_number_char + last_number_char
  two_digit_num = int(two_digit_char)
  values.append(two_digit_num)

result_part_one = sum(values)

print(result_part_one)

tokenizer = {
  0: "zero",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
}

def tokenize(line):
  for num, name in tokenizer.items():
    line = line.replace(name, f"{name}{num}{name}")
  return line

total = 0

for line in data:
  digits = [char for char in tokenize(line) if char.isdigit()]
  total += int(digits[0]+digits[-1])

print(total)