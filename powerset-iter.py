# python3 program for power set

import math

def printPowerSet(set,set_size):
  
  powerSet = []

  # set_size of power set of a set
  # with set_size n is (2**n -1)
  pow_set_size = (int) (math.pow(2, set_size))
  counter = 0
  j = 0

  # Run from counter 000..0 to 111..1
  for counter in range(0, pow_set_size):
    subSet = []
    for j in range(0, set_size):
  
      
      # Check if jth bit in the
      # counter is set If set then
      # print jth element from set
      if((counter & (1 << j)) > 0):
        subSet.append(set[j])
    powerSet.append(subSet)

  return powerSet

# Driver program to test printPowerSet
#set = ['a', 'b', 'c', 'd', 'e', 'f']

# If there's an adj pair mark invalid
def is_invalid(L):
  print("is invalid, L = ", L)

  for i in range(len(L)-1):

    print("L[i] = ", L[i])
    print("L[i+1] = ", L[i+1])

    if L[i]+1 == L[i+1]:
      return True

  return False


set = [1,2,3,4,5,6]

v = printPowerSet(set, 6)

print("len(v) = ", len(v))

v2 = []
for i in range(len(v) - 1):
  print("i = ", i)
  if is_invalid(v[i]):
    continue
  v2.append(v[i])

print("len(v) = ", len(v))

for s in v2:
    print(*s)

# This code is contributed by mits.
