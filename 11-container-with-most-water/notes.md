## Intuition
The area of water between two lines depends on both the width (distance between them) and the height (limited by the shorter line). Starting with maximum width and strategically reducing it toward taller lines gives us the best chance of finding the largest area.

## Implementation
Place left and right pointers at opposite ends of the array. Calculate the current area using `width * min(height[l], height[r])` and track the maximum. Move the pointer pointing to the shorter line inward—if `height[l] > height[r]`, decrement `r`; otherwise, increment `l`. This ensures we always explore potentially larger areas.

## Edge-cases
No special edge cases. The algorithm naturally handles arrays of any valid length.

## Complexity
- Time: `O(n)` — each pointer moves at most n times
- Space: `O(1)` — only tracking pointers and max area
