<div align="center">
    <h1>lcnotes</h1>
    <p>CLI to create dedicated Python environments and run/test Leetcode problems with documentation</p>
</div>

## Problems Solved
| Problem | Notes | Difficulty | Solution |
| :-----: | ----- | :--------: | :------: |
| [1. Two Sum](https://leetcode.com/problems/two-sum) | - **Intuition**: To find a valid answer for a given number, we just need to check if it's complement is in the array (i.e. target - curr)<br />- **Implementation**: Use a hash map to store numbers with indices, for each number, check if complement = target - curr is in the map, return<br />- **Edge-Cases**: Make sure to check the indices are not the same to ensure not using the same number (map[complement] != i)<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./two-sum/solution.py)
