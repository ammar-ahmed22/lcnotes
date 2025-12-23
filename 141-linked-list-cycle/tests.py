import pytest
from solution import Solution
from lcutils import ListNode

@pytest.mark.parametrize("head, pos, expected", [
    (ListNode.create(3, 2, 0, 4), 1, True),
    (ListNode.create(1, 2), 0, True),
    (ListNode.create(1), -1, False)
])
def test_linked_list_cycle(head, pos, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    updated = ListNode.add_cycle(head, pos)
    assert solution.hasCycle(updated) == expected
