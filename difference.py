# xor-sum

# find integer x in range[0,k] with max xor-sum value
# xor-sum(x) = {x xor A[0]} + {x xor A[1]} + {x xor A[2} + ....

# n=int(input("No of elements"))
# k=int(input("k: "))
# for i in range(0,k):


# print(n)
# 

# if * > # => positive integer
# if # > * => negative integer
# if * == # => 0

n='**##*#*#**####*'
hashmap={}

for i in n:
  if i in hashmap:
    hashmap[i]+=1
  else:
    hashmap[i]=0

result=hashmap['*']-hashmap['#']
print(result)