## Intuition
The area is determined by width (distance between lines) and height (the shorter of the two lines). Starting with maximum width (pointers at both ends), we can only potentially increase area by finding a taller line, so always move the pointer pointing to the shorter line inward.

## Implementation
Place left and right pointers at the array ends. Calculate area using the minimum height times the width. Move the pointer at the shorter line toward the center, as keeping it could only decrease the area. Track the maximum area seen.

## Edge-cases
When both heights are equal, it doesn't matter which pointer moves since neither can form a larger area with the current other side.

## Complexity
Time `O(n)` for a single pass with two pointers. Space `O(1)` using only pointers.
