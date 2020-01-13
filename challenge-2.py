def makeFibbo(num):
  start = [0,1]
  startNum = start[-1]
  for i in range(num):
    start.extend([startNum])
    startNum += start[-2]
  evenNums = [i for i in start[2:] if i % 2 == 0]
  return sum(evenNums)

print(makeFibbo(43))