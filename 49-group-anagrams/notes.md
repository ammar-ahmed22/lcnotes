## Intuition
All anagrams share the same character frequency distribution. If we can create a canonical representation of this frequency, we can use it as a key to group anagrams together in a hashmap.

## Implementation
For each string, build a frequency table (26-element array for lowercase letters). Use this frequency table as a hashmap key, with the value being a list of strings that share that frequency signature. After processing all strings, return the hashmap values as the grouped anagrams.

## Edge-cases
Python dictionaries don't allow lists as keys, so convert the frequency table to a comma-separated string (e.g., "1,0,1,0,...") to use as the key.

## Complexity
Time `O(n * k)` where n is the number of strings and k is the maximum string length. Space `O(n)` for the hashmap storing all strings.
