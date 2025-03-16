n = int(input())

in_ = n*2-3
out_ = 0

for i in range(n-1):
    print(' '*out_+'*'+' '*in_+'*')
    out_+=1
    in_ -=2

print(' '*out_+'*')
out_-=1
in_ +=2
for i in range(n-1):
    print(' '*out_+'*'+' '*in_+'*')
    out_-=1
    in_+=2

# output
'''
n = 6
	
*         * 
 *       *  
  *     *   
   *   *    
    * *     
     *      
    * *     
   *   *    
  *     *   
 *       *  
*         * 
'''