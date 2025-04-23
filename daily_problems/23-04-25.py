
# You are given an integer n.

# Each number from 1 to n is grouped according to the sum of its digits.

# Return the number of groups that have the largest size.

 

# Example 1:

# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
# Example 2:

# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
 

# Constraints:

# 1 <= n <= 104
#mysolution
class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict

        def digit_sum(x):
            return sum(int(d) for d in str(x))
    
        group_counts = defaultdict(int)
    
        for i in range(1, n + 1):
            s = digit_sum(i)
            group_counts[s] += 1
    
        max_size = max(group_counts.values())
        return sum(1 for count in group_counts.values() if count == max_size)
    
#Solution 2.
class Solution(object):
    def countLargestGroup(self, n):
        sums = [0] * 37
        for i in range(1, n + 1):
            sums[self.digsum(i)] += 1

        maxi, count = 0, 0
        for i in sums:
            if i > maxi:
                maxi, count = i, 1
            elif i == maxi:
                count += 1
        return count

    def digsum(self, n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s