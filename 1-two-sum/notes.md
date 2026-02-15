## Intuition
The key insight is that for any number in the array, we need to find if its complement (target minus that number) exists elsewhere in the array. Rather than searching for the complement with nested loops, we can use a hashmap for constant-time lookups.

## Implementation
First, populate a hashmap with each number as the key and its index as the value. Since the problem guarantees exactly one solution with distinct indices, we can safely overwrite duplicate values. Then iterate through the array again, computing the complement for each number and checking if it exists in the map.

## Edge-cases
When checking for the complement in the map, ensure the found index is different from the current index. This prevents returning the same element twice (e.g., if target is 6 and we have a 3, we shouldn't return [0, 0]).

## Complexity
Time `O(n)` for two passes through the array. Space `O(n)` for the hashmap storing all elements.
