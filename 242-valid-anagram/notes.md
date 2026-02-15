## Intuition
Two strings are anagrams if they contain exactly the same characters with the same frequencies. Rather than sorting both strings and comparing, we can use a frequency count approach that's more efficient.

## Implementation
Since the input only contains lowercase English letters, use a fixed-size array of 26 elements as a frequency counter. Increment the count for each character in the first string, then decrement for each character in the second string. If the strings are anagrams, all counts will return to zero.

## Edge-cases
Strings of different lengths cannot be anagrams, though this is implicitly handled by the frequency counting approach.

## Complexity
Time `O(n)` for iterating through both strings. Space `O(1)` since the frequency array is always 26 elements regardless of input size.
