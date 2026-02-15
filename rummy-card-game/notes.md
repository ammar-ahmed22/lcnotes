## Intuition
Rummy melds are either sets (3+ cards of same rank, different suits) or runs (3+ consecutive cards of same suit). Group cards by rank for sets and by suit for runs, then generate all valid combinations.

## Implementation
Group cards into two hashmaps: by rank and by suit. For sets, generate all combinations of 3+ cards with the same rank. For runs, sort cards by rank within each suit, find consecutive sequences, and generate all windows of 3+ consecutive cards.

## Edge-cases
Only process groups with at least 3 cards. When building consecutive sequences, flush the current segment when a gap is found, then start a new segment.

## Complexity
Time `O(n^2)` due to generating combinations. Space `O(n^2)` for storing all possible melds.
