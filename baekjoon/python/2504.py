ps = raw_input()
if len(ps) % 2 == 1:
  print(0)
else:
  s = 0
  d = 0
  stack = []
  r = [0] * 16
  for p in ps:
    if p == ')' and stack and stack[-1] == '(':
      stack.pop()
      r[len(stack)] += 2
    elif p == ']' and stack and stack[-1] == '[':
      stack.pop()
      r[len(stack)] += 3
    
    else:
      stack.append(p)
  print(s)

  # (()[[]])([])
  # 2
  # 22
  # 