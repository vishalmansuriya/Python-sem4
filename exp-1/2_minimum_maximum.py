# Given an array arr[]. Your task is to find the minimum and maximum elements 
# in the array. 
# Examples: 
# Input: arr[] = [1, 4, 3, 5, 8, 6] 
# Output: [1, 8] 
# Explanation: minimum and maximum elements of array are 1 and 8.


arr= [1, 4, 3, 5, 8, 6]
max=arr[0]
min=arr[0]

for i in range(0,len(arr)):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        mix=arr[i]

print(f"[{max},{min}]")