## Intuition
To achieve O(n) time, we can't sort. Instead, identify sequence starting points—numbers that have no predecessor (n-1 not in array). From each starting point, count how far the sequence extends.

## Implementation
Store all numbers in a hashset for O(1) lookups. Iterate through the array and for each number, check if it's a sequence start (n-1 doesn't exist). If it is, count consecutive numbers starting from it by repeatedly checking for n+1, n+2, etc. Track the maximum sequence length found.

## Edge-cases
Duplicates can cause the same sequence to be processed multiple times. Mark sequence starts as processed after handling them to avoid redundant work.

## Complexity
Time `O(n)` because each number is visited at most twice (once in the main loop, once when extending a sequence). Space `O(n)` for the hashset.
