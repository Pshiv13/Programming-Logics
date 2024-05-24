''' You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too. '''

## Prepare a count list where it will store the count of the alphabet
## use l and r pointer and r will go to right side.
## if r-l+1 - max(count) > k then it is invalid and do l+=1
## Update longest path every time

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count = [0]*26

        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1
            while (r-l+1) - max(count) > k:
                count[ord(s[l])-65] -= 1
                l+=1
            longest = max(longest, (r-l)+1)
        return longest
