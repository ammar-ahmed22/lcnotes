## Intuition
Use three pointers: left marks the start of a character group, right scans for the group's end, and write tracks where to put the compressed output. Compress in-place by overwriting the input array.

## Implementation
For each group of consecutive identical characters: (1) advance right until the character changes, (2) write the character at the write pointer, (3) if the count > 1, write each digit of the count. Then move left to right's position and repeat.

## Edge-cases
When count > 9, write each digit separately (e.g., 12 becomes '1' then '2'). Single-character groups don't need a count.

## Complexity
Time `O(n)` processing each character once. Space `O(1)` modifying the array in place.
