''' Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. '''

## Using sliding window algo
## use set. if not in set then move r otherwise remove l and move l (l+=1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxl = 0,0,0
        c = set()

        while(r<len(s)):
            if s[r] not in c:
                maxl = max(maxl, r-l+1)
                c.add(s[r])
                r+=1
            else:
                c.remove(s[l])
                l+=1
        return maxl
      
