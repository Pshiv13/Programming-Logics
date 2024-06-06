''' In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1 '''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = []
        for i in range(1, n+1):
            a.append(i)
        
        t = []
        for i in range(len(trust)):
            t.append(trust[i][0])
        
        if len(set(a) - set(t)) != 1: return -1
        else: 
            for i in range(1, n+1):
                if i == list(set(a) - set(t))[0]: continue
                if [i, list(set(a) - set(t))[0]] not in trust: return -1
            return list(set(a) - set(t))[0]
