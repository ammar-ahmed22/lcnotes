## Intuition
The key insight is that for any number in the array, we need to check if its complement (`target - curr`) exists elsewhere. Rather than using a nested loop to search for each complement, we can use a hashmap to achieve constant-time lookups.

## Implementation
First, populate a hashmap with all numbers and their indices, allowing overwrites since duplicates won't be part of the answer. Then iterate through the array again, computing each number's complement and checking if it exists in the map. If found, return the pair of indices.

## Edge-cases
The main edge case is ensuring that the complement isn't the number itself. Always verify that `map[complement] != i` before returning—this prevents using the same element twice.

## Complexity
- Time: `O(n)` — two passes through the array
- Space: `O(n)` — hashmap stores up to n elements
