def multiplesOf3and5(num):
  return sum([i for i in range(num) if i % 3 == 0 or i % 5 == 0])

print(multiplesOf3and5(8456))