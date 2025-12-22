import pytest
from solution import Solution
from lcutils import arr_to_list, list_to_str

@pytest.mark.parametrize("head, expected", [
    (arr_to_list([1, 2, 3, 4, 5]), arr_to_list([5, 4, 3, 2, 1])),
    (arr_to_list([1, 2]), arr_to_list([2, 1])),
])
def test_reverse_linked_list(head, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    received = solution.reverseList(head)
    assert list_to_str(received) == list_to_str(expected)
