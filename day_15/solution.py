with open ("day_15/data.txt") as f:
  data = f.read()

def hash(string):
  value = 0

  for ch in string:
    value += ord(ch)
    value *= 17
    value %= 256

  return value

print(sum(map(hash, data.split(","))))