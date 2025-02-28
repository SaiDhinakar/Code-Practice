n = int(input())

for i in range(1,n+1):
    c = 64
    print(' '*(n-i),end='')
    for j in range(i*2-1):
        if j > ((i*2-1)//2):
            c-=1
            print(chr(c),end='')
        else:
            c+=1
            print(chr(c), end='')
    print()

# output:

'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
'''