## Intuition
We're searching for the minimum eating speed that allows finishing within h hours. The answer lies between 1 and max(piles). Binary search works because if speed k works, all speeds > k also work—the answer space is monotonic.

## Implementation
Binary search on speed from 1 to max(piles). For each candidate speed, calculate total hours needed (sum of ceil(pile/speed) for each pile). If hours exceed h, we need faster eating—search higher. Otherwise, search lower to find the minimum valid speed.

## Edge-cases
Use ceiling division when calculating hours per pile since Koko can't eat a fractional pile and must spend at least one hour on any non-empty pile.

## Complexity
Time `O(n log m)` where n is number of piles and m is max pile size. Space `O(1)`.
