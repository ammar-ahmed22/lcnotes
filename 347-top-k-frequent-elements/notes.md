## Intuition
Instead of sorting by frequency (which would be O(n log n)), we can use bucket sort. Since the maximum frequency of any element is bounded by the array length n, we can create an array where the index represents the frequency and the value is a list of elements with that frequency.

## Implementation
First, count frequencies using a hashmap. Then create a bucket array of size n+1, where each index i contains elements that appear exactly i times. Finally, iterate backwards from the highest frequency bucket, collecting elements until we have k items.

## Edge-cases
Multiple elements can share the same frequency, so each bucket must be a list rather than a single value. When collecting results, iterate through each bucket's contents before moving to the next.

## Complexity
Time `O(n)` for counting and bucket distribution. Space `O(n)` for the frequency map and bucket array.
