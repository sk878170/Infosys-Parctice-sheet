# bubble_sort

def bubble_sort(arr):
  n=len(arr)
  for j in range(len(arr)):
    for i in range(0,len(arr)-1,1):
      if arr[i]>arr[i+1]:
        temp=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=temp
      else:
        pass
  return arr

arr=[5,1,3,2,6,-1,7,-2]
print(bubble_sort(arr))



      