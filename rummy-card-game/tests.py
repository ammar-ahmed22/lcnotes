import pytest
from solution import Solution

@pytest.mark.parametrize("cards, expected", [
    (["1C", "9C", "8C", "7C", "5C", "4C", "9D", "9S", "1D", "1H"], [["1C", "1D", "1H"], ["9C", "9D", "9S"], ["7C", "8C", "9C"]]),
    (["4C", "2C", "3C", "1C", "8D", "6C", "9D", "9C", "1D", "1H"], [["1C", "1D", "1H"], ["1C", "2C", "3C"], ["2C", "3C", "4C"], ["1C", "2C", "3C", "4C"]])
])
def test_rummy_card_game(cards, expected):
    solution = Solution()
    result = solution.findMelds(cards)
    sorted_result = result
    for meld in sorted_result:
        meld.sort()
    sorted_result.sort()

    sorted_expected = expected
    for meld in sorted_expected:
        meld.sort()
    sorted_expected.sort()

    assert sorted_result == sorted_expected
