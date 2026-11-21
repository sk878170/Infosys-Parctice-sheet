# Problem: Find All Subarrays with a Given Sum
# Given an integer array nums of size N and an integer target, find and print all contiguous subarrays whose sum is equal to the given target.

# A subarray is a continuous sequence of elements from the original array.

# input
# nums = [3, 4, -7, 1, 3, 3, 1, -4]
# target = 7

# output
# [3, 4]
# [3, 4, -7, 1, 3, 3]
# [4, -7, 1, 3, 3, 1, -4]
# [7]


nums = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7

n = len(nums)
result = []

for i in range(0,n,1): # 0 to 8 
    temp = []
    total = 0

    for j in range(i, n): 
        temp.append(nums[j])
        total += nums[j]

        if total == target:
            print(temp)
            result.append(temp.copy())

print(result)
