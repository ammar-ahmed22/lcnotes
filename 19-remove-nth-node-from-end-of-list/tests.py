import pytest
from solution import Solution
from lcutils import ListNode

@pytest.mark.parametrize("head, n, expected", [
    (ListNode.create(1, 2, 3, 4, 5), 2, ListNode.create(1, 2, 3, 5)),
    (ListNode.create(1), 1, None),
    (ListNode.create(1, 2), 1, ListNode.create(1)),
])
def test_remove_nth_node_from_end_of_list(head, n, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert str(solution.removeNthFromEnd(head, n)) == str(expected)
