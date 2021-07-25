# def selection_sort(arr):
#     n = len(arr)
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1,n):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#         arr[i],arr[min_index] = arr[min_index],arr[i]
#     print(arr)

# def counting_sort(arr):
#     n = len(arr)
#     res = [0]*n
#     max = 0
#     for i in range(n):
#         if arr[i] >= max:
#             max = arr[i]
#     c = [0]*(max+1)
#     for i in arr:
#         c[i]+= 1
#     print(c)
#     for i in range(1,max+1):
#         c[i] = c[i]+c[i-1]
#     print(c)
#     i = n-1
#     while i>=0:
#         res[c[arr[i]]-1] = arr[i]
#         c[arr[i]]-=1
#         i-=1
#     print(res)
# a = [1,2,4,6,1,2,5,3,4]
# counting_sort(a)

# def radix_sort(arr):
#     max = 0
#     for i in range(len(arr)):
#         if arr[i] > max:
#             max= arr[i]
#     d = 1
#     while max//d >0:
#         counting_sort(arr,d)
#         d = d*10
        
        
# def counting_sort(arr,d):
#     n = len(arr)
#     res = [0]*n
#     c = [0]*10
#     for i in range(0,n):
#         temp = arr[i]//d
#         c[temp%10]+=1
#     for i in range(1,10):
#         c[i] = c[i]+c[i-1]
#     i = n-1
#     while i>=0:
#         temp = arr[i]//d
#         res[c[temp%10]-1] = arr[i]
#         c[temp%10]-=1
#         i-=1
#     for i in range(n):
#         arr[i] = res[i]

# a = [12,15,111,7,14567]
# radix_sort(a)
# print(a)
# def shell_sort(arr,n):
#     gap = n//2
#     while gap>0 :
#         for i in range(gap,n):
#             anchor = arr[i]
#             j = i
#             while j >= gap and arr[j-gap]>anchor:
#                 arr[j] = arr[j-gap]
#                 j-=gap
#             arr[j] = anchor
#         gap = gap//2
#     print(arr)

# a = [21,34,-15,-0.3,0.7]
# shell_sort(a,5)

# def bubble_sort(arr,n):
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[i]
#     print(arr)
# bubble_sort([1,5,7,8,4,2],6)


# def insertion_sort(arr,n):
#     for i in range(n):
#         val = arr[i]
#         j = i-1
#         while j>=0 and val < arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#             arr[j+1] = val
#     print(arr)

# insertion_sort([3,5,7,9,1,2,4],7)
# def merge_sort(arr):
#     n = len(arr)
#     if n>1:
#         mid = n//2
#         a = arr[:mid]
#         b = arr[mid:]
#         merge_sort(a)
#         merge_sort(b)
#         i,j,k = 0,0,0
#         while i<len(a) and j<len(b):
#             if a[i] > b[j]:
#                 arr[k] = b[j]
#                 k+=1
#                 j+=1
#             elif a[i]<= b[j]:
#                 arr[k] = a[i]
#                 k+=1
#                 i+=1
#         while i < len(a):
#             arr[k] = a[i]
#             k+=1
#             i+=1
#         while j < len(b):
#             arr[k] = b[j]
#             k+=1
#             j+=1
#     return arr
# def quick_sort(arr,left,right):
#     if left <right:
#         partition_pos = partition(arr,left,right)
#         quick_sort(arr,left,partition_pos-1)
#         quick_sort(arr,partition_pos+1,right)

# def partition(arr,left,right):
#     i = left
#     j = right-1
#     pivot = arr[right]
#     while i<j:
#         while i<right and arr[i]<pivot:
#             i+=1
#         while j> left and arr[j]>=pivot:
#             j-=1
#         if i<j:
#             arr[i],arr[j] = arr[j],arr[i]
#     if arr[i] > pivot:
#         arr[i],arr[right] = arr[right],arr[i]
#     return i
# a = [12,14,3,6,8,15,51,-53]
# quick_sort(a,0,len(a)-1)
# print(a)