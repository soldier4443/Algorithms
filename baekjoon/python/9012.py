n = int(raw_input())
r = ''
for _ in xrange(n):
  ps = raw_input()
  if len(ps) % 2 == 1:
    r += "NO\n"
    continue
  cnt = 0
  for p in ps:
    if p == '(':
      cnt += 1
    else:
      cnt -= 1
    if cnt < 0:
      break
  r += "NO\n" if cnt else "YES\n"

print(r)