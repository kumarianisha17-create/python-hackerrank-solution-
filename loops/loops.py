# Task
# The provided code stub reads an integer,n , from STDIN. For all non-negative integers i<n, print i power 2.

# Example:
# n = 3
# The list of non-negative integers that are less than  n = 3 is [0,1,2].
# Print the square of each number on a separate line.

# 0
# 1
# 4

# Input Format

# The first and only line contains the integer,n .
# Constrains :
# 1<= n<=20

# output format:
# Print n lines, one corresponsing to each i.

# Sample Input 0
# 5

# Sample Output 0
# 0
# 1
# 4
# 9
# 16



if __name__ == '__main__':
    n = int(input())
    if n>0:
        for i in range(0,n):
            square=i*i
            print(square)