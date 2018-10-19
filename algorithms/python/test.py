import sort
import read
import unittest
import random

class SortTest(unittest.TestCase):
  def test_bubbleSort(self):
    items = [5, 1, 2, 4, 3]
    sort.bubbleSort(items)
    self.assertListEqual(items, [1, 2, 3, 4, 5])

if __name__ == '__main__':
  unittest.main()