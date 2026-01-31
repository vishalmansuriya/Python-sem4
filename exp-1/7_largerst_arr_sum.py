# You are given an integer array arr[]. You need to find the maximum sum of a 
# subarray (containing at least one element) in the array arr[]. 
# Note : A subarray is a continuous part of an array. 
# Examples: 
# Input: arr[] = [2, 3, -8, 7, -1, 2, 3] 
# Output: 11 
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11. 


        
arr = [2, 3, -8, 7, -1, 2, 3]
current_sum=arr[0]
max_sum=arr[0]
for i in range(1,len(arr)):
    if (current_sum+arr[i])>arr[i]:
        current_sum+=arr[i]
    else:
        current_sum=arr[i]
    if current_sum>max_sum:
        max_sum=current_sum
# print(current_sum)
print(max_sum)

