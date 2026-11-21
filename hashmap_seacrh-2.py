nums=[1,3,5,7,-9]

pos=[0]*10000
neg=[0]*10000

for i in nums:
  if i>0:
    pos[i]+=1
  elif i<0:
    neg[i]+=1
  else:
    pos[0]+=1

print(pos[:10])
print(neg[:10])

x=int(input("Enter element ot be searched: "))
if x>0 and pos[x]>=1:
  print("found")
elif x<0 and neg[x]>=1:
  print("found")

else:
  print("not found")