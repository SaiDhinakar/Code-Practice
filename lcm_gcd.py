def GCD(*nums):
    if len(nums)<2:
        print("Invalid Inputs!")
        return
    
    def findGCD(a,b):
        return b if a==0 else findGCD(b%a,a)

    res = nums[0]
    for num in nums[1:]:
        res = findGCD(num, res)
        
        if res == 1:
            return 1
    return res

def LCM(*nums):
    if len(nums)<2:
        print("Invalid Inputs!")
        return

    res = GCD(*nums)
    lcm = nums[0]
    for i in nums:
        lcm *= i // res
    return lcm//res

print(LCM(25,15,5))