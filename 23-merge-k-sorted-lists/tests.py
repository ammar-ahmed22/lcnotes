import pytest
from solution import Solution
from lcutils import ListNode

@pytest.mark.parametrize("lists, expected", [
    ([ListNode.create(1, 4, 5), ListNode.create(1, 3, 4), ListNode.create(2, 6)], ListNode.create(1,1,2,3,4,4,5,6)),
    ([], None),
])
def test_merge_k_sorted_lists(lists, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert str(solution.mergeKLists(lists)) == str(expected)
