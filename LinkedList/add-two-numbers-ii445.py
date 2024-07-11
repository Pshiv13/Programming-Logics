''' You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1 = []
        L2 = []

        while l1:
            L1.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            L2.append(str(l2.val))
            l2 = l2.next
        
        S1 = "".join(L1)
        S2 = "".join(L2)
        SUM = int(S1) + int(S2)

        LL = list(str(SUM))
        N = len(LL)
        D = ListNode()
        H = D

        for i in range(N):
            H.next = ListNode(int(LL[i]))
            H = H.next
        
        return D.next
