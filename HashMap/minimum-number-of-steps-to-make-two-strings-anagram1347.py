""" You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s. """


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        S = set(list(s))
        ANS = 0

        for i in S:
            p = s.count(i)
            q = t.count(i)

            if q >= p:
                continue
            else:
                ANS += p - q

        return ANS
