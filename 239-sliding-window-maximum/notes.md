## Intuition
Use a monotonic decreasing deque that stores indices. The front always holds the maximum for the current window. Remove elements from the back that are smaller than the incoming element (they can never be the maximum), and remove from the front when indices fall outside the window.

## Implementation
Maintain a deque of indices in decreasing order of their values. For each new element: (1) remove smaller elements from the back, (2) add the current index, (3) remove the front if it's outside the window, (4) once the window reaches size k, record the front as the maximum.

## Edge-cases
The deque stores indices, not values—this allows checking whether elements have left the window. Only start recording answers once the window has reached full size (when r + 1 >= k).

## Complexity
Time `O(n)` since each element is added and removed from the deque at most once. Space `O(k)` for the deque.
