def work(numbers):
  stack = []
  prints = ''
  ptr = 0
  for k in numbers:
    if ptr < k:
      while ptr < k:
        ptr += 1
        prints += '+\n'
        stack.append(ptr)

    if stack[-1] == k:
      stack.pop()
      prints += '-\n'
    else:
      return "NO"
  return prints

n = int(raw_input())
numbers = [int(raw_input()) for i in range(0, n)]
prints = work(numbers)

print(prints)