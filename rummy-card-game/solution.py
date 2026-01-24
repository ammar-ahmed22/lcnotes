from typing import List, Tuple
from collections import defaultdict
from itertools import combinations

class Solution:
    def findMelds(self, cards: List[str]) -> List[List[str]]:
        def parseCard(card: str) -> Tuple[int, str]:
            return (int(card[0]), card[1])

        # Group cards by rank and suit
        # Space: O(n) -> all cards are stored
        by_rank = defaultdict(list)
        by_suit = defaultdict(list)
        # Time: O(n)
        for card in cards:
            rank, suit = parseCard(card)
            by_rank[rank].append(card)
            by_suit[suit].append(card)


        result = []

        # Find sets
        for rank in by_rank:
            rank_cards = by_rank[rank]
            # Only care about ranks that have 3 or more cards
            if len(rank_cards) < 3:
                continue
            # Create sets using combinations of 3+ cards
            for n in range(3, len(rank_cards) + 1):
                for combo in combinations(rank_cards, n):
                    result.append(list(combo))
        # Find runs
        for suit in by_suit:
            suit_cards = by_suit[suit]
            # Only care about suits that have 3 or more cards
            if len(suit_cards) < 3:
                continue
            # Sort cards by rank
            ranked = sorted([(parseCard(c)[0], c) for c in suit_cards], key=lambda x: x[0])

            # Build consecutive segments
            segments: List[Tuple[int, str]] = []

            for r, c in ranked:
                if not segments:
                    segments.append((r, c))
                else:
                    prev_r = segments[-1][0]
                    if r == prev_r + 1:
                        segments.append((r, c))
                    else:
                        # Add windows of consecutive segments to result and flush
                        if len(segments) >= 3:
                            seg_cards = [card for _, card in segments]
                            m = len(seg_cards)
                            for i in range(m):
                                for j in range(i + 3, m + 1):
                                    result.append(seg_cards[i:j])
                        segments = [(r, c)]
            # Flush the any remaining segment
            if len(segments) >= 3:
                seg_cards = [card for _, card in segments]
                m = len(seg_cards)
                for i in range(m):
                    for j in range(i + 3, m + 1):
                        result.append(seg_cards[i:j])

        return result

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
    test = ["1C", "9C", "8C", "7C", "5C", "4C", "9D", "9S", "1D", "1H"]
    print(solution.findMelds(test))
