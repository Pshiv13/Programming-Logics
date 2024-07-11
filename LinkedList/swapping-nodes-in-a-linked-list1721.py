''' You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]'''

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        D = head
        L = 0

        while D:
            L += 1
            D = D.next
        
        F = k-1
        S = L-k

        D1, D2 = head, head

        for _ in range(F):
            D1 = D1.next

        for _ in range(S):
            D2 = D2.next
        
        temp1 = D1.val
        D1.val = D2.val
        D2.val = temp1

        return head
