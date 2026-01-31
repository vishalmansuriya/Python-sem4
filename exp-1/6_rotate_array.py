# Given an array arr, rotate the array by one position in clockwise direction. 
# Examples: 
# Input: arr[] = [1, 2, 3, 4, 5] 
# Output: [5, 1, 2, 3, 4] 

arr=[1, 2, 3, 4, 5] 
# print(len(arr))
# print()
last_value=arr[-1]
for i in range(len(arr)-1,0,-1):
    # print(i)
    arr[i]=arr[i-1]
arr[0]=last_value
print(arr)
