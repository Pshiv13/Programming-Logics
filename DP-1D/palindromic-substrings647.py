""" Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the 
same backward as forward. A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c". """

## Similar to palindromic sub string, just pick one char and check l and r whether same or not and increament a counter.
## Do it for ODD and EVEN len of palindromic string


class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            ## Odd Len
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1

            ## Even Len
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
        return c
