def TwoSum(nums, target):
    seen = {}
    for idx, num in enumerate(nums):
        complement = target-num
        if complent in seen:
            return [seen[complement], idx]
        seen[num] = i
    return [-1,-1]

# inputs
nums = list(map(int, input().split()))
target = int(input())

print(TwoSum(nums, target))
