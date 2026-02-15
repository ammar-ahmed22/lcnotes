## Intuition
A number is the start of a consecutive sequence if there's no number exactly one less than it in the array. Once we identify a sequence start, we can count how long the sequence extends by checking for consecutive numbers.

## Implementation
Store all numbers in a hashmap for `O(1)` lookup. Iterate through the array and check if each number is a sequence start (`num - 1` not in map). If it is, walk forward counting consecutive numbers (`num + 1`, `num + 2`, etc.) and track the maximum length found.

## Edge-cases
Duplicates can cause us to process the same sequence start multiple times. Initialize the hashmap with all `False` values and mark a sequence start as `True` once processed to avoid redundant work.

## Complexity
- Time: `O(n)` — each number is part of at most one sequence traversal
- Space: `O(n)` — hashmap stores all numbers
