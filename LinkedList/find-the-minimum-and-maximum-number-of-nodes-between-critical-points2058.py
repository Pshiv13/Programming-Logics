''' A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance
between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points.
If there are fewer than two critical points, return [-1, -1]. '''

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        CP = []
        L = 0
        D = head

        while D:
            L+=1
            D = D.next
        
        P = head
        C = head.next
        N = head.next.next
        pos = 1

        for i in range(L-2):
            if C.val > P.val and C.val > N.val:
                CP.append(pos)
            elif C.val < P.val and C.val < N.val:
                CP.append(pos)
            P = P.next
            C = C.next
            N = N.next
            pos += 1

        if len(CP) < 2:
            return [-1, -1]
        
        minD = float('inf')
        maxD = CP[-1] - CP[0]

        for i in range(1, len(CP)):
            minD = min(minD, CP[i] - CP[i-1])

        return [minD, maxD]
