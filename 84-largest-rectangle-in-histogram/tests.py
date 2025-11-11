import pytest
from solution import Solution

# iter 1, stack = []
# empty, push to stack with index (2, 0)
# iter 2, stack = [(2, 0)]
# curr < stack[-1], pop, calc max area, push new
# iter 3, stack = [(1, 1)]
# curr >= stack[-1], push
# iter 3, stack = [(1, 1), (5, 2)]
# curr >= stack[-1], push [(1, 1), (5, 2), (6, 3)]
# iter 4, stack = [(1, 1), (5, 2), (6, 3)]

# steps
# 1. initialize stack
# 2. iterate
# if curr is less than stack top, iterate while curr < stack.top, pop from the top and keep track of max area, height is the min value, width is distance from curr index to popped index
# if curr is >= stack top, push value and index

# worst case -> O(n^2)

@pytest.mark.parametrize("heights, expected", [
    ([2,1,5,6,2,3], 10),
    ([2, 4], 4)
])
def test_largest_rectangle_in_histogram(heights, expected):
    # Write your test assertions here
    # e.g. for twoSum, assert sorted(solution.twoSum(nums, target)) == sorted(expected)
    solution = Solution()
    assert solution.largestRectangleArea(heights) == expected
