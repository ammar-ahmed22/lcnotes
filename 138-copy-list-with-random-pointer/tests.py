import pytest
from solution import Solution, Node

@pytest.mark.parametrize("input", [
    ([[7,None],[13,0],[11,4],[10,2],[1,0]]),
    ([[1,1],[2,1]]),
    ([[3,None],[3,0],[3,None]]),
])
def test_copy_list_with_random_pointer(input):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()

    # Create the linked list from the input list
    nodes = [Node(val) for val, _ in input]
    for i, (_, random_index) in enumerate(input):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    head = nodes[0] if nodes else None
    copied_head = solution.copyRandomList(head)

    # Assert that the copied list has the same structure as the input
    # (We use input directly since the original list may be corrupted)
    current_copied = copied_head
    copied_nodes = []
    while current_copied:
        copied_nodes.append(current_copied)
        current_copied = current_copied.next

    assert len(copied_nodes) == len(input)
    for i, (val, random_index) in enumerate(input):
        assert copied_nodes[i].val == val
        if random_index is not None:
            assert copied_nodes[i].random is copied_nodes[random_index]
        else:
            assert copied_nodes[i].random is None
