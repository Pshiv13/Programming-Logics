""" You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step"""

# Using recursion


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Memoriazation Top down


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def f(n):
            if n in memo:
                return memo[n]

            else:
                memo[n] = f(n - 1) + f(n - 2)
                return memo[n]

        return f(n)


# Bottom up with tabulation


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]


# Bottom up with constant space


class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2

        if n == 1:
            return one
        if n == 2:
            return two

        for i in range(n - 2):
            one, two = two, one + two

        return two
