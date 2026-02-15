## Intuition
A monotonic decreasing deque maintains potential maximums in order. When a larger element enters, smaller elements can never be the maximum for any future window, so we remove them.

## Implementation
Use a deque storing indices. For each new element, pop from the back while the deque's back value is smaller than the current element (they're no longer useful). Add the current index. If the front index is outside the window (`l > q[0]`), pop it from the front. Once we've processed at least k elements (`r + 1 >= k`), the front of the deque is the maximum—add it to the result and slide the window.

## Edge-cases
The deque stores indices rather than values, which makes it easy to check if elements are still within the window bounds.

## Complexity
- Time: `O(n)` — each element is added and removed from deque at most once
- Space: `O(k)` — deque holds at most k elements
