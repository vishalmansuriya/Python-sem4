# Given a sorted array of distinct integers and a target value, return the index if the 
# target is found. If not, return the index where it would be if it were inserted in 
# order. 
# You must write an algorithm with O(log n) runtime complexity. 
  
# Example 1: 
# Input: nums = [1,3,5,6], target = 5 
# Output: 2

nums=[1,3,55,6]
target=int(input("Enter number: "))
# target=5

left=0
right=len(nums)-1

while left<=right:
    mid=int((left+right)/2)
    if nums[mid]==target:
        print(f"value found at index i = {mid}") 
        break 
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print(f"target insert at index i = {left}")
# print(left)
# print(right)
        