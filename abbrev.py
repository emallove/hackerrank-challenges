#!/bin/python3

# You can perform the following operations on the string, :
# 
# Capitalize zero or more of 's lowercase letters.  Delete all of the remaining
# lowercase letters in .  Given two strings,  and , determine if it's possible
# to make  equal to  as described. If so, print YES on a new line. Otherwise,
# print NO.
# 
# For example, given  and , in  we can convert  and delete  to match . If  and ,
# matching is not possible because letters may only be capitalized or discarded,
# not changed.
# 
# Function Description
# 
# Complete the function  in the editor below. It must return either  or .
# 
# abbreviation has the following parameter(s):
# 
# a: the string to modify b: the string to match Input Format
# 
# The first line contains a single integer , the number of queries.
# 
# Each of the next  pairs of lines is as follows: - The first line of each query
# contains a single string, .  - The second line of each query contains a single
# string, .
# 
# Constraints
# 
# String  consists only of uppercase and lowercase English letters,
# ascii[A-Za-z].  String  consists only of uppercase English letters,
# ascii[A-Z].  Output Format
# 
# For each query, print YES on a new line if it's possible to make string  equal
# to string . Otherwise, print NO.
# 
# Sample Input
# 
# 1 daBcd ABC Sample Output
# 
# YES Explanation
# 
# image
# 
# We have  daBcd and  ABC. We perform the following operation:
# 
# Capitalize the letters a and c in  so that  dABCd.  Delete all the remaining
# lowercase letters in  so that  ABC.  Because we were able to successfully
# convert  to , we print YES on a new line.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def traverse_grid(a, b):
    i = 0
    j = 0

    while (i <= len(a)) and (j <= len(b)):

      # We've gone off the lower-right diagonal of the grid
      if i >= len(a) and j >= len(b):
        return True

      print("line 38:  i = ", i)
      print("line 38:  j = ", j)

      # We exhausted just one of the lists, so we're 
      if i >= len(a):
        # We CAN NOT delete a trailing capital letter
        if b[j].isupper():
          return False
        # We CAN delete a trailing capital letter
        else:
          j += 1

      # We exhausted just one of the lists, so we're 
      if j >= len(b):
        # We CAN NOT delete a trailing capital letter
        if a[i].isupper():
          return False
        # We CAN delete a trailing capital letter
        else:
          i += 1
          
      if (i >= len(a)) or (j >= len(b)):
        break

      print("line 52: i = ", i)
      print("line 52: j = ", j)

      # effectively change the letter, if it's lower          
      if (a[i] == b[j]) or (a[i].upper() == b[j]):

        print("line 58: a[i] = ", a[i])
        print("line 58: b[j] = ", b[j])

        i += 1
        j += 1

      # effectively delete the letter, if it's lower          
      elif a[i].islower():
          i += 1
      else:
        return False
  
    return True
 
def upperOrDelete(frag, target):

    print("frag = ", frag)
    print("target = ", target)

    if "".join(frag) == "".join(target):
      return True

    if "".join(frag) == "":
      return True

    if (frag[0].islower()):
 
      if len(frag) > 0:

        char1 = [frag[0].upper()]
        frag1 = char1 + frag[1:len(frag)]
        frag2 =  frag[1:len(frag)]
 
        print("frag1 = ", frag1)
        print("frag2 = ", frag2)

        # Uppercased char recursion
        r1 = upperOrDelete(frag1, target)

        # Deleted char recursion
        r2 = upperOrDelete(frag2, target)

      else:
        return False
      
      return r1 or r2

def abbreviation(a, b):
 
    r = upperOrDelete(list(a), list(b))
    print("r = ", r)
    
    if r:
      return "YES"
    else:
      return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
