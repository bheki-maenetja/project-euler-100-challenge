from math import log

def check_if_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def smallestMult(num):
  nums = [i for i in range(2, num + 1)]
  prime_nums = [i for i in range(2, num + 1) if check_if_prime(i)]
  result_nums = [(x//y, y) for x in nums for y in prime_nums if log(x) % log(y) == 0]
  print(nums, prime_nums, result_nums)

smallestMult(13)