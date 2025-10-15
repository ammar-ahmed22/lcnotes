- **Intuition**: Since array is sorted, we only need to look for our complment (`target - curr`) in the values to the right of the current (also sorted, binary search)
- **Implementation**: For each number, calculate the complement, conduct binary search on the elements to the right of it, if not found keep going, if found return

