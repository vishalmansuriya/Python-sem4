# Given an integer array arr[] and an integer k, your task is to find and return 
# the kth smallest element in the given array. 
# Note: The kth smallest element is determined based on the sorted order of the 
# array. 
# Examples : 
# Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4 
# Output: 5 

arr=[10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
# arr=list(set(arr)) #remove dup
number=int(input("Enter kth smallest number: "))
arr.sort()
print(arr)
print(arr[number-1])