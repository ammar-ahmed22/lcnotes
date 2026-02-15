## Intuition
Bucket sort by frequency. Since the maximum frequency is n, we can use an array where index represents frequency and values are the elements with that frequency. Scanning from highest to lowest frequency gives us the top k elements.

## Implementation
First, count frequencies with a hashmap. Then create a frequency array of length `n + 1` (indices 0 to n), where each index is a list of elements with that frequency. Iterate backward through this array, collecting elements until we have k items.

## Edge-cases
Multiple elements can share the same frequency, so each bucket is a list. When collecting results, iterate through all elements in each bucket before moving to the next lower frequency.

## Complexity
- Time: `O(n)` — frequency counting and bucket iteration
- Space: `O(n)` — hashmap and frequency buckets
