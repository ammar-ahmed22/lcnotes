## Intuition
To detect duplicates, we need to remember which numbers we've seen. A hashmap provides `O(1)` lookup to check if a number has appeared before.

## Implementation
Iterate through the array. For each number, check if it's already in the hashmap—if so, we found a duplicate, return `True`. Otherwise, add the number to the map and continue. If the loop completes, no duplicates exist, return `False`.

## Edge-cases
An empty array or single-element array has no duplicates by definition. The algorithm handles these naturally.

## Complexity
- Time: `O(n)` — single pass with O(1) lookups
- Space: `O(n)` — hashmap stores up to n elements
