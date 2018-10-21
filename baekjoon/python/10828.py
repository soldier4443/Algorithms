n = int(raw_input())
stack = []

for i in range(0, n):
  commands = raw_input().split()
  cmd = commands[0]
  if cmd == "push":
    stack.append(int(commands[1]))
  elif cmd == "pop":
    print(-1 if len(stack) == 0 
             else stack.pop())
  elif cmd == "top":
    print(-1 if len(stack) == 0 
             else stack[-1])
  elif cmd == "size":
    print(len(stack))
  elif cmd == "empty":
    print(1 if len(stack) == 0 
            else 0)
