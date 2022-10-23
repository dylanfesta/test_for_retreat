
import numpy as np

c1 = 123.456
c2 = np.sqrt(c1)

def do_something_one():
    print('Function called from Package one! All good!')


def error_maybe():
  x = 1
  y = 2
  z = 'hello world'
  if x == 1:
    raise Exception('Error!')
  return  
