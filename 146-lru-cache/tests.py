import pytest
from solution import LRUCache

@pytest.mark.parametrize("commands, params, output", [
    (["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
     [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
     [None, None, None, 1, None, -1, None, -1, 3, 4]),
])
def test_lru_cache(commands, params, output):
    cache = LRUCache(0)
    for cmd, param, expected in zip(commands, params, output):
        match cmd:
            case "LRUCache":
                cache = LRUCache(*param)
                assert expected is None
                break
            case "put":
                cache.put(*param)
                assert expected is None
                break
            case "get":
                result = cache.get(*param)
                print(result)
                assert result == expected, f"Expected {expected} but got {result} for get"
                break
