# python3 program for power set

# 
# 
# Given an array of integers, find the subset of non-adjacent elements with the
# maximum sum. Calculate the sum of that subset. It is possible that the maximum
# sum is , the case when all elements are negative.
# 
# Example
# 
# The following subsets with more than  element exist. These exclude the empty
# subset and single element subsets which are also valid.
# 
# Subset      Sum
# [-2, 3, 5]   6
# [-2, 3]      1
# [-2, -4]    -6
# [-2, 5]      3
# [1, -4]     -3
# [1, 5]       6
# [3, 5]       8 The maximum subset sum is . Note that any individual element is
# a subset as well.
# 
# 
# In this case, it is best to choose no element: return .
# 
# Function Description
# 
# Complete the  function in the editor below.
# 
# maxSubsetSum has the following parameter(s):
# 
# int arr[n]: an array of integers
# Returns
# - int: the maximum subset sum
# 
# Input Format
# 
# The first line contains an integer, .
# The second line contains  space-separated integers .
# 
# Constraints
# 
# Sample Input 0
# 
# 5
# 3 7 4 6 5
# Sample Output 0
# 
# 13
# Explanation 0
# 
# Our possible subsets are  and . The largest subset sum is  from subset 
# 
# Sample Input 1
# 
# 5
# 2 1 5 8 4
# Sample Output 1
# 
# 11
# Explanation 1
# 
# Our subsets are  and . The maximum subset sum is  from the first subset listed.
# 
# Sample Input 2
# 
# 5
# 3 5 -7 8 10
# Sample Output 2
# 
# 15
# Explanation 2
# 
# Our subsets are  and . The maximum subset sum is  from the fifth subset listed.

import math

# Return true if the bit string contains adjacent set bits
def contains_adj_set_bits(b, bits):
  for i in range(bits):
    if ((b & (1 << i)) and (b & (i << (i+1)))):
      return True

  return False

def get_power_set(my_set):

  set_size = len(my_set)

  powerSet = []

  # set_size of power my_set of a my_set
  # with set_size n is (2**n -1)
  pow_set_size = (int) (math.pow(2, set_size))
  counter = 0
  j = 0

  # Run from counter 000..0 to 111..1
  for counter in range(0, pow_set_size):
    subSet = []
    for j in range(0, set_size):

      # Check if jth bit in the counter is set, then get jth element from
      # my_set.
      if not contains_adj_set_bits(counter, set_size):
        if ((counter & (1 << j)) > 0):
          subSet.append(my_set[j])

    powerSet.append(subSet)

  return powerSet

# If there's an adj pair mark invalid
def contains_an_adjacent_pair(L):

  for i in range(len(L) - 1):
    if L[i]+1 == L[i+1]:
      return True

  return False

def getSeq(v):
  r = []
  for i in range(v):
    r.append(i)
  return r

# Get sub-set of sets based on indicies,
# e.g., [0,2,4] of [0,1,2,3,4,5] returns [0,2,4]
def getSubSet(indicies, sets):

  r = []
  for i in indicies:
    r.append(sets[i])

  return r

def maxSubsetSum(mainSet):

  indiciesPowerSet = getSeq(len(mainSet))
  indiciesPowerSet = get_power_set(indiciesPowerSet)

  acceptableSets = []

  # Remove pairs which contain an adjacency
  for ithSubSet in indiciesPowerSet:

    if contains_an_adjacent_pair(ithSubSet):
      continue

    subset = getSubSet(ithSubSet, mainSet)
    acceptableSets.append(subset)

  # Find the max of the valid sub-lists
  _max = 0
  for s in acceptableSets:
      _sum = sum(s)
      if _sum > _max:
        _max = _sum

  return _max


sample_input_2 = [3,5,-7,8,10]
random_org_sample = [38, 12, 52, 93, 82, 21, 25, 71, 87, 98, 28, 89, 65, 86, 22, 15, 23, 14]

seq_size = len(random_org_sample)
print("seq_size = ", seq_size)

import cProfile
cProfile.run('v = maxSubsetSum(random_org_sample)')
#v = maxSubsetSum(random_org_sample)
print("v = ", v)
