## Intuition
Maintaining a max heap of length k will keep the k smallest elements in it.

## Implementation
Define a function to calculate the distance for a point to the origin. A small optimization we can make is using the squared distance instead of the actual Euclidean distance. Since, we calculate them all the same way and we only care about comparing their relative magnitude's against each other, this is fine. The optimization we get from this is saving on the slightly expensive square root calculation. For the distance to origin, the squared distance is just `x^2 + y^2`.

After this, we initialize our max heap. In Python, the `heapq` implementation is a min heap by default. To make it a max heap, we can simply negate the heap key (distance) for it to become a max heap.

Iterate over the points:
- Calculate the distance for the point
- Add the distance (negated) and the point to the heap (`heapq.heappush(heap, (-d, point))`)
- If the length of the heap exceeds `k`, pop from the heap (this will maintain a length of `k` for the heap, keeping the points with the k smallest distances)

At the end, construct the list of points from the heap that have the k smallest distances and return.

## Complexity
- Time: `O(n log k)`, we iterate over all the points once and and our heap operations are worst-case, `O(log k)` because the heap does not exceed length `k`.
- Space: `O(k)`, only extra space created is the heap which is max length `k`.
