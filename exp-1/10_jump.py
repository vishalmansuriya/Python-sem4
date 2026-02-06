# You are given an array arr[] of non-negative numbers. Each number tells you 
# the maximum number of steps you can jump forward from that position. 
# For example: 
# • If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i. 
# 2 
# • If arr[i] = 0, you cannot jump forward from that position. 
# Your task is to find the minimum number of jumps needed to move from 
# the first position in the array to the last position. 
# Note:  Return -1 if you can't reach the end of the array. 
# Examples :  
# Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9] 
# Output: 3  
# Explanation: First jump from 1st element to 2nd element with value 3. From here 
# we jump to 5th element with value 9, and from here we will jump to the last. 


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
if n == 1:
    print(0)
elif arr[0] == 0:
    print(-1)
else:
    jumps = 1
    steps = arr[0]
    maxReach = arr[0]
    for i in range(1, n):
        # If reached last index(just check if we are on last index)
        if i == n - 1:
            print(jumps)
            break
        # Update how far we can go (just update maxReach)
        maxReach = max(maxReach, i + arr[i])
        # Use one step
        steps -= 1
        # If no steps left, take a jump
        if steps == 0:  
            jumps += 1
            # If we are stuck
            if i >= maxReach:
                print(-1)
                break
            # Reset steps
            steps = maxReach - i
