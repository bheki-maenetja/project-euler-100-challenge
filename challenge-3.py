def check_if_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def getLargestFactor(num):
  primeNums = [i for i in range(2, num + 1) if num % i == 0 and check_if_prime(i)]
  return primeNums

print(getLargestFactor(100))