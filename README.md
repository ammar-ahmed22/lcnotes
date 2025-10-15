<div align="center">
    <h1>lcnotes</h1>
    <p>CLI to create dedicated Python environments and run/test Leetcode problems with documentation</p>
</div>

## Problems Solved
| Problem | Notes | Difficulty | Solution |
| :-----: | ----- | :--------: | :------: |
| [1. Two Sum](https://leetcode.com/problems/two-sum) | - **Intuition**: To find a valid answer we simply need to find if the complement (`target - curr`) exists in the array<br />- **Implementation**: Use a hashmap to store numbers with their indices (allow overwrites because duplicates are not allowed), check if the complement exists in the map and is not the same number, return<br />- **Edge-cases**: Ensure that you check the indices are not the same when returning (i.e. `map[complement] != i`)<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./1-two-sum/solution.py)
