n = int(input())

c = 65 + n-1

for i in range(n):
    ch = c
    for j in range(i+1):
        print(chr(ch),end=' ')
        ch+=1
    c-=1
    print()

# output:
'''
E 
D E 
C D E 
B C D E 
A B C D E 
'''