## Intuition
To detect duplicates efficiently, we need a way to quickly check if we've seen a number before. A hashmap provides O(1) lookups, making it ideal for tracking previously encountered values.

## Implementation
Iterate through the array, checking each number against a hashmap. If the number already exists in the map, we've found a duplicate—return True immediately. Otherwise, add the number to the map and continue. If the loop completes without finding any duplicates, return False.

## Edge-cases
No special edge cases beyond empty arrays, which would simply return False since there's nothing to duplicate.

## Complexity
Time `O(n)` for a single pass through the array. Space `O(n)` for the hashmap in the worst case where all elements are unique.
