n = int(input()) # n = 3

for top in range(2*n-1):
    for bottom in range(2*n-1):
        right = (2*n-2)-bottom
        left = (2*n-2)-top
        print(n- min(min(top,bottom), min(left,right)),end=' ')
    print()

# output
'''
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
'''