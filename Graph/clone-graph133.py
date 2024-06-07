''' Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 
Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph. '''

# Using DFS and mark the nodes visited
# First create all the cloned nodes and then mark the relations between them using hash map

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        start = node
        old_to_new = {}
        visited = set()
        visited.add(start)
        st = [start]

        while st:
            node = st.pop()
            old_to_new[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    st.append(nei)
        
        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])
        
        return old_to_new[start]
