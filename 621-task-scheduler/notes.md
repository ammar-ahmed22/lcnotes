## Intuition
To minimize total time, we should always execute the most frequent remaining task. When all available tasks are cooling down, we must idle until one becomes ready. A max heap lets us greedily pick the most frequent task at each step, and a cooldown queue tracks tasks waiting to be re-added.

## Implementation
Count task frequencies, then build a max heap from the counts (negated for Python's min heap).

Maintain a `cooldown_q` deque of `(remaining_count, available_at_time)` pairs. Simulate time `t`:
- Each loop iteration increments `t` by 1.
- If the heap is empty (all tasks cooling down), jump `t` directly to `cooldown_q[0][1]` to skip idle time.
- Otherwise, pop the most frequent task, decrement its count, and if it still has remaining executions, append `(count, t + n)` to the cooldown queue.
- After processing, if the front of the cooldown queue has `available_at_time == t`, pop it and push its count back onto the heap.

Return `t` when both the heap and cooldown queue are empty.

## Edge-cases
When the heap is empty but the cooldown queue is non-empty, jumping `t` directly to `cooldown_q[0][1]` avoids simulating each idle tick individually—but we still only do this when the heap is empty, since if tasks are available we should execute them instead.

## Complexity
- Time: `O(n)` where `n` is total number of tasks. Heap operations are constant because the heap will be at most 26 values.
- Space: `O(1)`, heap size is, at most, 26 values.
