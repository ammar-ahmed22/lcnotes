import pytest
from solution import Solution

@pytest.mark.parametrize("points, k, expected", [
    ([[1,3],[-2,2]], 1, [[-2,2]]),
    ([[3,3],[5,-1],[-2,4]], 2, [[-2,4],[3,3]]),
])
def test_k_closest_points_to_origin(points, k, expected):
    solution = Solution()
    assert sorted(solution.kClosest(points, k)) == sorted(expected)
