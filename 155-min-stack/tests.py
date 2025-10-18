import pytest
from solution import MinStack

@pytest.mark.parametrize("calls, args, expected", [
    (["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]], [None,None,None,None,-3,None,0,-2]),
    (["MinStack","push","push","push","getMin","pop","getMin","pop","getMin","pop","push","push","push","getMin","pop","top","getMin","pop","getMin","pop"], [[],[0],[1],[0],[],[],[],[],[],[],[-2],[-1],[-2],[],[],[],[],[],[],[]], [None,None,None,None,0,None,0,None,0,None,None,None,None,-2,None,-1,-2,None,-2,None])
])
def test_min_stack(calls, args, expected):
    min_stack = MinStack()
    for call, arg, exp in zip(calls, args, expected):
        if call == "MinStack":
            continue
        assert getattr(min_stack, call)(*arg) == exp
