def binary_search(nums,x):
  i=0
  j=len(nums)-1
  found=0

  while i<=j:
    mid=(i+j)//2
    if nums[mid]==x:
      found=1
      return "found"

    elif x>nums[mid]:
      i=mid+1

    else:
      j=mid-1
  return "not found"



nums=[1,2,3,4,5]
print(binary_search(nums,6))
      