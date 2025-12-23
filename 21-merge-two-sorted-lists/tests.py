import pytest
from solution import Solution
from lcutils import ListNode

@pytest.mark.parametrize("list1, list2, expected", [
    (ListNode.create(1, 2, 4), ListNode.create(1, 3, 4), ListNode.create(1, 1, 2, 3, 4, 4)),
    (None, None, None),
    (None, ListNode.create(0), ListNode.create(0)),
])
def test_merge_two_sorted_lists(list1, list2, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    received = solution.mergeTwoLists(list1, list2)
    assert str(received) == str(expected)
