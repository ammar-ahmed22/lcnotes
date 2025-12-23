import pytest
from solution import Solution
from lcutils import ListNode 

@pytest.mark.parametrize("head, expected", [
    (ListNode.create(1, 2, 3, 4, 5), ListNode.create(5, 4, 3, 2, 1)),
    (ListNode.create(1, 2), ListNode.create(2, 1)),
])
def test_reverse_linked_list(head, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    received = solution.reverseList(head)
    assert str(received) == str(expected)
