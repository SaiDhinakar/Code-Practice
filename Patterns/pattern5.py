n = int(input()) # n = 5

for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range((i*2)-1):
        print('*',end='')
    print()

# output:
'''
    *
   ***
  *****
 *******
*********
'''

for i in range(n,0,-1):
    print(' '*(n-i),end='')
    for j in range((i*2)-1):
        print('*',end='')
    print()

# output:
'''
*********
 *******
  *****
   ***
    *
'''