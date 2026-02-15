## Intuition
Springs should be used for the largest height differences to maximize distance. Greedily use sandbags first, then retroactively convert the largest sandbag uses to springs when sandbags run out.

## Implementation
Use a max heap (via negation in Python) to track height differences. For each upward jump, initially use sandbags and push the difference to the heap. When sandbags go negative, convert the largest previous sandbag use to a spring by popping from the heap and restoring those sandbags.

## Edge-cases
If sandbags go negative and no springs remain, return the current index—we can't proceed further. Python uses min heap, so negate values for max heap behavior.

## Complexity
Time `O(n log n)` for n heap operations. Space `O(n)` for the heap.
