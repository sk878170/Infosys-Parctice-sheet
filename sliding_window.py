# You are given an array of integers, arr,
# and an integer k. Your task is to find and print the maximum number in
# each contiguous window of size k.
# Sample test case 1:
# Input:
# arr = [1, 3, -1, -3, 5, 3, 6, 7] k=3
# Output:
# [3, 3, 5, 5, 6, 7]
###

arr = [1, 3, -1, -3, 5, 3, 6, 7] 
k=3
res=[]
for i in range(0,len(arr)-2,1):
  sub_arr=arr[i:i+k]
  res.append(max(sub_arr))

print(res)
  

  