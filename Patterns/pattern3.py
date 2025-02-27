n = int(input()) # n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

#output:
'''
1
12
123
1234
12345
'''

for i in range(1,n+1):
    print(f'{i}'*i)

# output:
'''
1
22
333
4444
55555
'''