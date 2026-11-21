nums=[1,2,3,4,5,6,2]

hashmap={}
count={}
for i in range(0,len(nums)-1,1):
  if nums[i] not in hashmap:
    hashmap[nums[i]]=i

for i in nums:
  if i not in count:
    count[i]=1
  else:
    count[i]+=1

x=int(input("Enter the element to be found : "))
if x in hashmap:
  print("found at",hashmap[x])
  print("count :",count[x])
else:
  print("not found")