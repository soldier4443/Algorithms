n = int(raw_input())
numbers = []
for i in range(0, n):
  numbers.append(int(raw_input()))

def calculateCounts(number):
  memo = [0] * 41
  def fibo(n):
    if n <= 1:
      return n
    else:
      if memo[n] == 0:
        memo[n] = fibo(n - 1) + fibo(n - 2)
      return memo[n]
  
  if number == 0:
    return 1, 0
  else:
    return fibo(number - 1), fibo(number)

for number in numbers:
  zeros, ones = calculateCounts(number)
  print zeros, ones