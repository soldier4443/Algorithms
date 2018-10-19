import time

def measureTime(callable, name = "", log = False):
  start = time.time()
  callable()
  end = time.time()
  elapsed = end - start
  if (log):
    print("Time takes {0:02.6f}ms for task {1}".format(elapsed, name))
  return elapsed