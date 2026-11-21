#  insertion sort

def insertion_sort(arr):
  for i in range(1,len(arr)):
    temp=arr[i]
    j=i-1
    print("temp=",temp)
    print("j=",j)
    while j>=0 and temp<arr[j]:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=temp
  return arr

arr=[5,1,3,2,4,7,9,8]
print(insertion_sort(arr))


