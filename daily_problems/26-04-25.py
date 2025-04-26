# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
# Example 2:

# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

# Constraints:

# 2 <= nums.length <= 105
# 1 <= nums[i], minK, maxK <= 106

def countSubarrays(nums: list[int], minK: int, maxK: int) -> int:
    total = 0
    last_bad = -1  # Index of the last element outside [minK, maxK]
    last_min = -1  # Index of the last minK
    last_max = -1  # Index of the last maxK
    
    for i, num in enumerate(nums):
        if num < minK or num > maxK:
            # Current element is outside the valid range, reset the window
            last_bad = i
            last_min = -1
            last_max = -1
        else:
            # Update positions of minK and maxK if found
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            
            # If both minK and maxK are present in the current window
            if last_min != -1 and last_max != -1:
                # The start of the subarray must be after last_bad
                # Count subarrays ending at i by taking the earliest index
                # where both minK and maxK are present
                total += min(last_min, last_max) - last_bad
    
    return total