import pytest
from solution import Solution
from lcutils import to_list, add_cycle

@pytest.mark.parametrize("head, pos, expected", [
    (to_list(3, 2, 0, 4), 1, True),
    (to_list(1, 2), 0, True),
    (to_list(1), -1, False)
])
def test_linked_list_cycle(head, pos, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    updated = add_cycle(head, pos)
    assert solution.hasCycle(updated) == expected
