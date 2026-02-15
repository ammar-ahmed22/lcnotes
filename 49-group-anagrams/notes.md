## Intuition
Anagrams have identical character frequencies. By using the frequency distribution as a key, all anagrams will hash to the same bucket.

## Implementation
Use a hashmap where keys represent frequency distributions and values are lists of anagrams. For each string, build a 26-element frequency array. Use this as the key to group strings together. Finally, collect all the values from the map as the result.

## Edge-cases
Python doesn't allow lists as dictionary keys. Convert the frequency array to a tuple or comma-separated string to make it hashable.

## Complexity
- Time: `O(n * k)` — where n is the number of strings and k is the maximum string length
- Space: `O(n * k)` — storing all strings in the hashmap
