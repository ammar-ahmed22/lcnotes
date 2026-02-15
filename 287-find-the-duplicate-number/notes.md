## Intuition
Treat the array as a linked list where each value points to the next index. A duplicate value means two indices point to the same location—forming a cycle. Finding the duplicate is equivalent to finding where the cycle begins.

## Implementation
Use Floyd's algorithm in two phases. Phase 1: fast and slow pointers starting at index 0, where the "next" of index i is nums[i]. They'll meet inside the cycle. Phase 2: reset one pointer to the start and move both at the same speed—they'll meet at the cycle's entrance, which is the duplicate.

## Edge-cases
The second phase is essential—the first meeting point is somewhere in the cycle, not necessarily at its start. The duplicate is specifically at the cycle entrance.

## Complexity
Time `O(n)` for both phases. Space `O(1)` using only pointers.
