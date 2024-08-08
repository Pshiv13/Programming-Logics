""" Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
Implement the Solution class:
Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen."""


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.Nodes = []

        while head:
            self.Nodes.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return self.Nodes[random.randint(0, len(self.Nodes) - 1)]
