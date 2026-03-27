import pytest
from solution import Solution

@pytest.mark.parametrize("tasks, n, expected", [
    (["A","A","A","B","B","B"], 2, 8),
    (["A","C","A","B","D","B"], 1, 6),
    (["A","A","A", "B","B","B"], 3, 10),
])
def test_task_scheduler(tasks, n, expected):
    solution = Solution()
    assert solution.leastInterval(tasks, n) == expected
