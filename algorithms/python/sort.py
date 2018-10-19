def bubbleSort(items):
  length = len(items)
  for i in range(0, length):
    for j in range(0, length - 1):
      if (items[j] > items[j+1]):
        items[j], items[j+1] = items[j+1], items[j]