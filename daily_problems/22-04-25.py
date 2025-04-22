# You are given two integers n and maxValue, which are used to describe an ideal array.

# A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

# Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
# Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
# Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 2, maxValue = 5
# Output: 10
# Explanation: The following are the possible ideal arrays:
# - Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
# - Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
# - Arrays starting with the value 3 (1 array): [3,3]
# - Arrays starting with the value 4 (1 array): [4,4]
# - Arrays starting with the value 5 (1 array): [5,5]
# There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
# Example 2:

# Input: n = 5, maxValue = 3
# Output: 11
# Explanation: The following are the possible ideal arrays:
# - Arrays starting with the value 1 (9 arrays): 
#    - With no other distinct values (1 array): [1,1,1,1,1] 
#    - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
#    - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
# - Arrays starting with the value 2 (1 array): [2,2,2,2,2]
# - Arrays starting with the value 3 (1 array): [3,3,3,3,3]
# There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
 

# Constraints:

# 2 <= n <= 104
# 1 <= maxValue <= 104

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        N = n + 15
        fact = [1] * (N + 1)
        invfact = [1] * (N + 1)

        for i in range(1, N + 1):
            fact[i] = fact[i-1] * i % MOD

        def mod_inverse(a, m):
            def pow_mod(base, exp, mod):
                base %= mod
                result = 1
                while exp > 0:
                    if exp & 1:
                        result = result * base % mod
                    base = base * base % mod
                    exp >>= 1
                return result
            return pow_mod(a, m - 2, m)

        invfact[N] = mod_inverse(fact[N], MOD)

        for i in range(N - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        def binomial(a: int, b: int) -> int:
            if a < b or b < 0:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

        total = 0
        for i in range(1, maxValue + 1):
            num = i
            product = 1
            p = 2
            while p * p <= num:
                if num % p == 0:
                    count = 0
                    while num % p == 0:
                        count += 1
                        num //= p
                    product = product * binomial(n + count - 1, n - 1) % MOD
                p += 1
            if num > 1:
                product = product * binomial(n, n - 1) % MOD
            total = (total + product) % MOD

        return total
    
# if __name__ == "__main__":
#     n = 5878
#     maxValue = 2900
#     sol = Solution()
#     result = sol.idealArrays(n, maxValue)
#     print(result)

        
        