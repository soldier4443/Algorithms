def naiveFibo(n):
  if n < 0:
    raise ValueError("n must be not negative")
  elif n <= 1:
    return n
  else:
    return naiveFibo(n - 1) + naiveFibo(n - 2)

def dynamicFibo(n):
  if n < 0:
    raise ValueError("n must be not negative")

  # Memorize every calculation results
  # -1 for default value
  memo = [-1] * (n + 1)

  for k in range(0, n + 1):
    if k <= 1:
      memo[k] = k
    else:
      memo[k] = memo[k - 1] + memo[k - 2]
  
  return memo[n]