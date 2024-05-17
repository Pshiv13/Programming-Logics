''' Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once. '''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)

        for x in s:
            a[x]+=1
        
        for z in t:
            a[z]-=1
        
        for v in a.values():
            if v!=0: return False
            
        return True
