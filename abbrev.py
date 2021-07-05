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
 

memo = dict()

# Change first lowercased letter to an upper-case letter
def upperFirstLower(s):
 
  for i in range(0, len(s)):
    
    if s[i].islower():
      s[i] = s[i].upper()
      break
      
  return s
  
# Delete first lower-cased lettter
def delFirstLower(s):
  
  for i in range(0, len(s)):
 
    if s[i].islower():
      del s[i]
      break
 
  return s
  
def _abbrev(frag, target):
  
  
    k = "".join(frag)
    if k in memo:
      return memo[k]
  
    # We found a match!
    if "".join(frag) == "".join(target):
      memo[k] = True
      return True
    
    # If it's not a match, and it can't be modified (because it's all uppercase),
    # then game over.
    elif "".join(frag).isupper():
      memo[k] = False
      return False

    frag1 = frag.copy()
    frag2 = frag.copy()
    
    frag1 = upperFirstLower(frag1)
    frag2 = delFirstLower(frag2)
 
    # Uppercased char recursion
    r1 = _abbrev(frag1, target)
    k = "".join(frag1)
    memo[k] = r1

    # Deleted char recursion
    r2 = _abbrev(frag2, target)
    k = "".join(frag2)
    memo[k] = r2

    return r1 or r2

def abbreviation(a, b):
 
    memo.clear()

    r = _abbrev(list(a), list(b))
    
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
