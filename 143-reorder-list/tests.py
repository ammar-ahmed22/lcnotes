import pytest
from solution import Solution
from lcutils import ListNode

@pytest.mark.parametrize("head, expected", [
    (ListNode.create(1, 2, 3, 4), ListNode.create(1, 4, 2, 3)),
    (ListNode.create(1, 2, 3, 4, 5), ListNode.create(1, 5, 2, 4, 3)),
])
def test_reorder_list(head, expected):
    solution = Solution()
    # modifies in-place
    solution.reorderList(head)
    assert str(head) == str(expected)
