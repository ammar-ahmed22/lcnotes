import pytest
from solution import Solution
from lcutils import ListNode

@pytest.mark.parametrize("l1, l2, expected", [
    (ListNode.create(2, 4, 3), ListNode.create(5, 6, 4), ListNode.create(7, 0, 8)),
    (ListNode.create(0), ListNode.create(0), ListNode.create(0)),
    (ListNode.create(9,9,9,9,9,9,9), ListNode.create(9,9,9,9), ListNode.create(8,9,9,9,0,0,0,1))
])
def test_add_two_numbers(l1, l2, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert str(solution.addTwoNumbers(l1, l2)) == str(expected)

