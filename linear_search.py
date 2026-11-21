#  linear search

def linear_search(arr,x):
  found=0
  for i in arr:
    if i==x:
      found=1

  if found==1:
    print("found")
  else:
    print("Not found")


nums=list(map(int, input().split()))
x=int(input("Enter the number to be found"))
linear_search(nums,x)