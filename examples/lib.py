
import random

def in_range(num, bottom, top):
  return (num - bottom) * (top - num) >= 0

def do_stuff():
  min = random.randint(1, 10000)
  max = random.randint(min, 10000)
  
  print("┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄\n")
  print('Press Ctrl+C, or enter NaN to exit', "\n")
  
  number = input("Enter number:\n")
  if number.isdigit():
    print('Number is in range' if in_range(int(number), min, max) else 'Number is out of range')
    print(" ", min, '..', max, sep=' ', end="\n")
  
  return number

# bound = 9999999999999

try:
  do_stuff()

  while True:
    number = do_stuff()
  
    # if number < (bound * -1) and number > bound:
    if not number.isdigit():
      print('Invalid string, NaN!', "\n")
      break
except KeyboardInterrupt:
  pass
  
print('Exit trigged')
  
exit(0)
