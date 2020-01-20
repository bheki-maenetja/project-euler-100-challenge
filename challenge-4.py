from math import sqrt, floor

def largestPalindromProduct(n):
  palindromes = [x * y for x in range(floor(sqrt(10 ** n)), 10 ** n) for y in range(floor(sqrt(10 ** n)), 10 ** n) if str(x * y) == str(x * y)[::-1]]
  print(max(palindromes))

largestPalindromProduct(4)

