import pytest
from solution import Solution
from lcutils import arr_to_list, list_to_str

@pytest.mark.parametrize("list1, list2, expected", [
    (arr_to_list([1, 2, 4]), arr_to_list([1, 3, 4]), arr_to_list([1, 1, 2, 3, 4, 4])),
    (None, None, None),
    (None, arr_to_list([0]), arr_to_list([0])),
])
def test_merge_two_sorted_lists(list1, list2, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    received = solution.mergeTwoLists(list1, list2)
    assert list_to_str(received) == list_to_str(expected)
