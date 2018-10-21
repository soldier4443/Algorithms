ps = input()
if len(ps) % 2 == 1:
  print(0)
else:
  stack = []
  r = [0] * 30
  for p in ps:
    co = 0
    if p == ')' and stack and stack[-1] == '(':
      co = 2
    elif p == ']' and stack and stack[-1] == '[':
      co = 3

    if co:
      stack.pop()
      l = len(stack)
      up = 1 if r[l+1] == 0 else r[l+1]
      r[l+1] = 0
      r[l] += co * up
    else:
      stack.append(p)
  if len(stack) == 0:
    print(r[0])
  else:
    print(0)
