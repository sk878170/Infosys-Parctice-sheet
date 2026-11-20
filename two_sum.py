# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twoSum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]]=i