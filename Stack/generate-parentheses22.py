""" Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"] """

# Using backtrack approach


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openCount, closeCount):
            if openCount == closeCount == n:
                res.append("".join(stack))
                return

            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(0, 0)
        return res
