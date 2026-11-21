# Wael is well-known for how much he loves the bit-wise XOR operation, while Kaito is well known for how much he loves to sum numbers, 
# so their friend Resli decided to make up a problem that would enjoy both of them. Resli wrote down an array A of length N, an integer K 
# and he defined a new function called Xor-sum as follows:

# Xor-sum(x) =(X XOR A[1])+(x XOR A[2])+(x XOR A[3])+ ........+(x XOR A[N])

n=3
k=7
arr=[1,6,3]
final=[]
for i in range(k):
  res=0
  for j in arr:
    res+=i ^ j
  final.append(res)
print(max(final))
  
    