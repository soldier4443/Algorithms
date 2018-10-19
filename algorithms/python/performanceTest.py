import util.measurements as msm
import fibonacci

def test_naiveFiboTime():
  n = 0
  while True:
    time = msm.measureTime(lambda: fibonacci.naiveFibo(n))
    if time >= 0.01:
      print("naiveFibo() calc limit: {}".format(n-1))
      break
    n += 1

def test_dynamicFiboTime():
  n = 0
  while True:
    time = msm.measureTime(lambda: fibonacci.dynamicFibo(n))
    if time >= 0.01:
      print("dynamicFibo() calc limit: {}".format(n-1))
      break
    n += 1

test_naiveFiboTime()
test_dynamicFiboTime()