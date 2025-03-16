n = int(input())

for i in range(n):
    if i==0 or i==n-1:
        print('* '*n)
    else:
        print(' '*(2*(n-i-1))+'*')


# Output
"""
n = 4
* * * *
    *
  *
* * * *
"""
