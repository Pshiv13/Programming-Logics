''' Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed). '''

# Using Fast and Slow Pointer. memory O(1)
# We know that at some point fast and slow pointer will always meet if there is a cycle.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True
        
        return False

# Using hashset. memory O(n)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = {}
        d = head
        while d:

            if d not in h: h[d] = None
            else: return True
            d = d.next
        
        return False
