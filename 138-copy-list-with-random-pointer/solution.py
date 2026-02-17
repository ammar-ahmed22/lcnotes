from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Optional['Node']= None, random: Optional['Node']= None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # interweave new nodes
        # i.e old1 -> new1 -> old2 -> new2 -> etc.
        curr = head
        while curr:
            next = curr.next
            curr.next = Node(curr.val, next)
            curr = next

        # assign random pointers
        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # construct resultant list
        curr = head.next if head else None
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head.next if head else None





if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
    input = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    nodes = [Node(val) for val, _ in input]
    for i, (_, random_index) in enumerate(input):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    head = nodes[0] if nodes else None
    solution.copyRandomList(head)
