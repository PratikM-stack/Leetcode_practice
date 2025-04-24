# You are given an array nums consisting of positive integers.

# We call a subarray of an array complete if the following condition is satisfied:

# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.

# A subarray is a contiguous non-empty part of an array.

 

# Example 1:

# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
# Example 2:

# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000
from collections import defaultdict

def countCompleteSubarrays(nums):
    # Get the number of distinct elements in the entire array
    target = len(set(nums))
    n = len(nums)
    count = 0
    freq = defaultdict(int)  # Frequency map for elements in the window
    
    left = 0
    for right in range(n):
        # Add the right element to the window
        freq[nums[right]] += 1
        
        # Check if the current window has the target number of distinct elements
        while len(freq) == target:
            # Count all subarrays starting from 'left' to at least 'right'
            # by shrinking the window from the left
            count += n - right  # All subarrays from 'left' to 'right' or beyond
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]  # Remove element if its frequency becomes 0
            left += 1
    
    return count