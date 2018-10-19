def items():
  print("Number of items: ")
  n = int(raw_input())
  return [int(raw_input()) for i in range(0, n)]