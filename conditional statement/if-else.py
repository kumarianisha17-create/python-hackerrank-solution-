# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5  to , print Not Weird
# If  even is even and in the inclusive range of 6 to 20  to , print Weird
# If n is even and greater than 20 , print Not Weird

# Input Format:
#     A single line containing a positive integer, n.

# Constraints
# 1<=n<=100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.


# Sample Input 0
# 3
# Sample Output 0
# Weird

# !/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n =int(input().strip())
    if n%2!=0:
        print("Weird")
    elif 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")



