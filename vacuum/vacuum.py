from itertools import accumulate
from operator import add

def parseFile(name):
  result = []
  with open(f'{name}.in') as reader:
    total = int(reader.readline())
    for _ in range(total):
      count = int(reader.readline()) # we do not need count
      numbers = list(map(int, reader.readline().split()))
      result.append((count, numbers))

  return result

def writeFile(name, values):
  with open(f'{name}.out', "w") as writer:
    for el in values:
      writer.write(str(el) + "\n")

def slow(c, values):
  if 0 in values:
    return "yes"
  
  for i in range(c - 1):
    sum = values[i]
    for j in range(i + 1, c):
      sum += values[j]
      if sum == 0:
        return "yes"
  
  return "no"

def fast(c, values):
  if 0 in values:
    return "yes"
  
  psums = list(accumulate(values, add))
  
  found = {}
  for el in psums:
    if not found.get(el):
      found[el] = True
    else:
      return "yes"
  
  return "no"

def main(filename):
  values = parseFile(filename)
  analyzed = [fast(c, v) for (c, v) in values]
  writeFile(filename, analyzed)

if __name__ == "__main__":
  main("large")