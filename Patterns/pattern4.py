n = int(input()) # n = 5

for i in range(n,0,-1):
    print('*'*i)

# output:
'''
*****
****
***
**
*
'''

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

# output:
'''
12345
1234
123
12
1
'''
