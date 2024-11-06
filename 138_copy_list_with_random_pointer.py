"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr_node = head
        # Note that we can put Node as a key because they are hashable by default. Each Node instance has a unique
        # memory address, which Python uses to compute its hash. This makes Node objects effectively immutable for
        # dictionary keys, even if their attributes (like next or random) change.
        old_to_new = {None: None}

        while curr_node:
            copy_node = Node(curr_node.val)
            old_to_new[curr_node] = copy_node
            curr_node = curr_node.next

        curr_node = head

        while curr_node:
            copy_node = old_to_new[curr_node]
            copy_node.next = old_to_new[curr_node.next]
            copy_node.random = old_to_new[curr_node.random]
            curr_node = curr_node.next

        return old_to_new[head]
