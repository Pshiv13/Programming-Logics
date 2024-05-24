"""Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer."""

## with brute force it will start from every char in string and go to o(n3) complexity
## try using left and right pointer and calculate palindromic using using the pointer as a middle char. l-- & r++
## Check for ODD and Even len Palindromic


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            ## For Odd len Palindromic
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
            # For even len Palindromic
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1

        return res
