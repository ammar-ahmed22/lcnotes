## Intuition
The eating speed ranges from 1 to max(piles). Binary search finds the minimum speed that lets Koko finish in time. Higher speeds always work if lower speeds work, so we're finding a threshold.

## Implementation
Binary search on speed from 1 to `max(piles)`. For each candidate speed, calculate total hours needed (sum of `ceil(pile/speed)` for each pile). If hours exceed h, we need more speed—search right. Otherwise, search left for potentially slower valid speeds. When the loop exits, `l` is the minimum valid speed.

## Edge-cases
Use ceiling division because even one banana in a pile takes a full hour. The answer is `l` at the end, not `r`.

## Complexity
- Time: `O(n log m)` — where m is max(piles), binary search with O(n) validation
- Space: `O(1)` — only tracking pointers
