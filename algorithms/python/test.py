import util.measurements as msm
import sort
import fibonacci
import unittest
import random

class SortTest(unittest.TestCase):
  def test_bubbleSort(self):
    items = [5, 1, 2, 4, 3]
    sort.bubbleSort(items)
    self.assertListEqual(items, [1, 2, 3, 4, 5])

class FiboTest(unittest.TestCase):
  def test_naiveFibo(self):
    self.assertEqual(fibonacci.naiveFibo(5), 5)
    self.assertEqual(fibonacci.naiveFibo(10), 55)
    self.assertEqual(fibonacci.naiveFibo(0), 0)
    self.assertEqual(fibonacci.naiveFibo(24), 46368)

  def test_dynamicFibo(self):
    self.assertEqual(fibonacci.dynamicFibo(5), 5)
    self.assertEqual(fibonacci.dynamicFibo(10), 55)
    self.assertEqual(fibonacci.dynamicFibo(0), 0)
    self.assertEqual(fibonacci.dynamicFibo(24), 46368)
    self.assertEqual(fibonacci.dynamicFibo(68), 72723460248141)

if __name__ == '__main__':
  unittest.main()