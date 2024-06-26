''' You are given a string s. Simulate events at each second i:
If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.
Example 1:
Input: s = "EEEEEEE"
Output: 7 '''

class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        c = 0

        for i in s:
            if i == "E":
                c+=1
                chair = max(c, chair)
            else:
                c-=1

        return chair
