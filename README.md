<div align="center">
    <h1>lcnotes</h1>
    <p>CLI to create dedicated Python environments and run/test Leetcode problems with documentation</p>
</div>

## Problems Solved
| Problem | Notes | Difficulty | Solution |
| :-----: | ----- | :--------: | :------: |
| [1. Two Sum](https://leetcode.com/problems/two-sum) | - **Intuition**: To find a valid answer we simply need to find if the complement (`target - curr`) exists in the array<br />- **Implementation**: Use a hashmap to store numbers with their indices (allow overwrites because duplicates are not allowed), check if the complement exists in the map and is not the same number, return<br />- **Edge-cases**: Ensure that you check the indices are not the same when returning (i.e. `map[complement] != i`)<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./1-two-sum/solution.py)
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate) | - **Intuition**: Need to check if a given number exists in the array<br />- **Implementation**: Use a hashmap, check if the current number is in the map, return True if found, otherwise add to map, return False at the end of loop (no duplicates found)<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./217-contains-duplicate/solution.py)
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram) | - **Intuition**: An anagram means the strings have the same frequency of letters, i.e. abc is anagram of bac or cab, etc.<br />- **Implementation**: Since only lowercase alphabet, increment in 26 value array at each character index (i.e. a = index 0, b = index 1, etc.) for `s` and decrement for `t`, if frequency array is zero, return True, otherwise False<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./242-valid-anagram/solution.py)
