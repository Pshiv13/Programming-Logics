''' Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: [] '''

## Use a dummy head, and left and right pointer with distance n between them. 
## Move right utill None or end of list

class Solution:       
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n>0 and right:
            n-=1
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
