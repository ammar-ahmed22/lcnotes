<div align="center">
    <h1>lcnotes</h1>
    <p>CLI to create dedicated Python environments and run/test Leetcode problems with documentation</p>
    <p>
      <img src="https://img.shields.io/badge/5-easy-green" />
      <img src="https://img.shields.io/badge/12-medium-yellow" />
      <img src="https://img.shields.io/badge/0-hard-red" />
    </p>
</div>

## Table of Contents
- [Problems Solved](#problems-solved)
- [Overview](#overview)
  * [How It Works](#how-it-works)
  * [Per-problem layout](#per-problem-layout)
- [Commands](#commands)
  * [add](#add)
  * [run](#run)
  * [test](#test)
  * [remove](#remove)
  * [publish](#publish)
  * [unpublish](#unpublish)
  * [generate-readme](#generate-readme)
- [Notes](#notes)

## Problems Solved
| Problem | Notes | Difficulty | Solution |
| :-----: | ----- | :--------: | :------: |
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams) | - **Intuition**: Every "group" of anagrams will have the same frequency table (26 value array)<br />- **Implementation**: Use a hashmap with the key being the frequency table and the value being the group of strings, iterate over each string, create the frequency table, check the map, add or create new entry in the map, finally take all the values from the map and flatten into a single result<br />- **Edge-cases**: Python doesn't allow arbitrary values as keys, convert frequency table to comma-separated string<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./49-group-anagrams/solution.py)
| [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements) | - **Intuition**: We can use an array that maps index to frequency (i.e. freq[1] = 2 means 2 has a frequency of 1), allowing us to formulate the answer in `O(n)` time<br />- **Implementation**: Use a hashmap to count frequencies, iterate over hashmap and create our frequency array (length `n + 1`, 1-based indexing), iterate backwards over frequency array to create result<br />- **Edge-cases**: Multiple elements can have the same frequency so frequency array should be an array of arrays, when iterating backwards go into arrays if needed<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./347-top-k-frequent-elements/solution.py)
| [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) | - **Intuition**: Use `prefix` and `suffix` arrays to calculate answer at each index. `prefix` is the product of all elements before `i` and `suffix` is the product of all elements after `i`.<br />- **Implementation**: Initialize `prefix` with `1` (before `i = 0` is just 1), iterate from `1 to n`, `prefix[i] = nums[i - 1] * prefix[i - 1]`. Initialize `suffix` with `suffix[-1] = 1` (after the end of the array, just 1 left), iterate backwards `n-2 to 0`, `suffix[i] = nums[i + 1] * suffix[i + 1]`. Answer is `ans[i] = prefix[i] * suffix[i]`<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./238-product-of-array-except-self/solution.py)
| [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku) | - **Intuition**: Check each row, column and 3x3 subbox for duplicates essentially<br />- **Implementation**: Use a hashmap to check for duplicates in each row, column and 3x3 subbox<br />- **Edge-cases**: Figuring out the indexing of the 3x3 subbox is difficult. Do 4 nested loops, `box_row (0 to 3)`, `box_col (0 to 3)`, `row (0 to 3)`, `col (0 to 3)`, then we can access the specific value with `board[3 * box_row + row][3  * box_col + col]`<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./36-valid-sudoku/solution.py)
| [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence) | - **Intuition**: The start of a sequence is when there IS a number exactly 1 greater than it in the array and NOT a number exactly 1 less than it. When a sequence start is found, iterate looking for the next values, keeping track of the max length<br />- **Implementation**: Use hashmap to store all numbers for `O(1)` lookup, iterate and look for sequence start, iterate building the sequence and keep track of max<br />- **Edge-cases**: In case of duplicates, we don't process the same sequence start multiple times. Initialize hashmap with all `False` values, when processing a sequence start, mark it as `True` to signify this sequence start is already processed and don't process that sequence start again<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./128-longest-consecutive-sequence/solution.py)
| [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) | - **Intuition**: Since array is sorted, we only need to look for our complment (`target - curr`) in the values to the right of the current (also sorted, binary search)<br />- **Implementation**: For each number, calculate the complement, conduct binary search on the elements to the right of it, if not found keep going, if found return<br /><br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./167-two-sum-ii-input-array-is-sorted/solution.py)
| [15. 3Sum](https://leetcode.com/problems/3sum) | - **Intuition**: Use a similar approach to [Two Sum II - Input Array Sorted](../167-two-sum-ii-input-array-is-sorted/solution.py), sort the input, look for when left and right of the right side of the array add up to the current number<br />- **Implementation**: Sort the input `O(n log n)`, for each number, binary search on the right side of the array, if `l + r = curr`, triplet found, add to result, move right if `l + r` is too big, otherwise move left<br />- **Edge-cases**: Ensure that we keep going even after finding a triplet because there could be more with the same `curr`. Also ensure that we move past duplicates for `curr` because it will be the same result, i.e. if we have [-1, -1, -1, 0, 1], we want to start processing at the last -1. Same thing when we find an answer, we want to move left and right until they are at the next non-duplicate<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./15-3sum/solution.py)
| [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water) | - **Intuition**: We want to maximize height and width. Start with max width and always reduce the width towards the larger height.<br />- **Implementation**: Left and right pointers at the end of the array. Keep track of max area using min of left and right as height. Move right or left pointer towards the larger one. i.e. if left > right, move right. if right > left, move left.<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./11-container-with-most-water/solution.py)
| [155. Min Stack](https://leetcode.com/problems/min-stack) | - **Intuition**: Use two stacks, one to track the min values and one for the actual stack<br />- **Implementation**: Initialize two stacks. `getMin` gets the top of the min stack if it has elements, otherwise top of main stack. `top` gets the top of the main stack always. `push` will always push to main stack, checks if the number is less than or equal to the min or if the stack is empty and pushes to the min stack, `pop` will check if the current top is equal to the min, pop from min stack, always pop from main stack after.<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./155-min-stack/solution.py)
| [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation) | - **Intuition**: In RPN, every operator operates on the last two elements while ensuring the results of all operations are continously updated.<br />- **Implementation**: Use a stack, whenever a number is seen, add to stack. When an operator seen, pop the last 2 and operate on them, push the result back to the stack and keep going. Return top of stack at the end.<br />- **Edge-cases**: In Python, integer division (`a // b`) does not truncate to zero, use `int(b / a)`. Remember order for division and subtraction matter, its `b - a` and `int(b / a)`.<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./150-evaluate-reverse-polish-notation/solution.py)
| [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | - **Intuition**: Recursively generate by going down the different possible paths to make a well-formed parentheses set. Open and closed must both equal n for it to be well-formed<br />- **Implementation**: Recursive function that takes open, closed, n, stack and result. Base case `open == close == n`, form the string from the stack and add to result. Otherwise, check if `open < n`, add open to stack, recurse with new count, pop from stack after to go down other path. Check if `closed < open` (other path), add close to stack, recurse with new count, pop from stack.<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./22-generate-parentheses/solution.py)
| [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures) | - **Intuition**: Store the temperature until a greater temperature is found.<br />- **Implementation**: Initialize result with all zeros, we will add in values when we find the larger one. Use a stack to store both temp and index, iterate, while stack is not empty and stack top temp is less than curr, pop from stack, calculate distance with indices, add to result at popped index. Add curr temp and index to stack.<br /> | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./739-daily-temperatures/solution.py)
| [1. Two Sum](https://leetcode.com/problems/two-sum) | - **Intuition**: To find a valid answer we simply need to find if the complement (`target - curr`) exists in the array<br />- **Implementation**: Use a hashmap to store numbers with their indices (allow overwrites because duplicates are not allowed), check if the complement exists in the map and is not the same number, return<br />- **Edge-cases**: Ensure that you check the indices are not the same when returning (i.e. `map[complement] != i`)<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./1-two-sum/solution.py)
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate) | - **Intuition**: Need to check if a given number exists in the array<br />- **Implementation**: Use a hashmap, check if the current number is in the map, return True if found, otherwise add to map, return False at the end of loop (no duplicates found)<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./217-contains-duplicate/solution.py)
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram) | - **Intuition**: An anagram means the strings have the same frequency of letters, i.e. abc is anagram of bac or cab, etc.<br />- **Implementation**: Since only lowercase alphabet, increment in 26 value array at each character index (i.e. a = index 0, b = index 1, etc.) for `s` and decrement for `t`, if frequency array is zero, return True, otherwise False<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./242-valid-anagram/solution.py)
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome) | - **Intuition**: Palindrome will have the same characters on the left and right side of the string when traversing at the same speed<br />- **Implementation**: Use right and left pointers, iterate towards the center, check if `l == r`, if not, early return `False`. Otherwise return `True`.<br />- **Edge-cases**: Can have non-alphanumeric or uppercase characters, make everything lowercase, skip over non-alphanumerics<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./125-valid-palindrome/solution.py)
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | - **Intuition**: Every opening bracket should eventually have a closing bracket that comes after it.<br />- **Implementation**: Use a stack and a map that maps opening brackets to closing, when seeing an opening bracket, push the closing bracket to the stack, When seeing a closing bracket, check the top of the stack, if its the same, pop and keep going, otherwise return `False`.<br />- **Edge-cases**: At the end, check the stack should be empty (unclosed brackets at the end). Also check if the stack is empty on seeing a closing bracket, return `False` there was no corresponding open.<br /> | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./20-valid-parentheses/solution.py)
---

## Overview
lcnotes is a personal CLI that helps me manage LeetCode problems locally. It can:
- Create a structured workspace for a problem (scraped metadata, starter code, docs, tests)
- Run or test solutions
- Track problems in a local problems.json
- Curate a README of published problems with notes and tags

### How it works (high level)
- Scraping: Uses Playwright to fetch title, difficulty, statement HTML, and Python starter code from LeetCode.
- Storage: problems.json tracks id, title, directory, difficulty, tags, notes, published.
- Templating: Jinja2 templates render docs and the top-level README.
- UX: Interactive fuzzy prompts for selecting problems; spinners for progress; consistent error handling.

### Per-problem layout
```text path=null start=null
<number>-<slug>/
  docs.md        # scraped problem statement (Markdown)
  notes.md       # personal notes; used when publishing
  solution.py    # starter code scaffold
  tests.py       # pytest tests scaffold
```

## Commands
Below are the CLI commands and what they do. If a slug is omitted or ambiguous, a fuzzy prompt lets me pick.

### add
Create a new workspace from a LeetCode slug.
- Fetch metadata (with spinner and retry), e.g. title, difficulty, statement, starter code
- Create the directory and files (docs.md, notes.md, solution.py, tests.py)
- Populate files from templates
- Add a base entry to problems.json

Usage:
```bash path=null start=null
lc add <problem-slug>
```

### run
Run solution.py for a problem (no tests; just executes the script).

Usage:
```bash path=null start=null
lc run [partial-slug]
```
- If not found or ambiguous, prompts to select a problem
- Executes: python3 <dir>/solution.py and prints stdout; exits non-zero on error

### test
Run pytest tests for a problem.

Usage:
```bash path=null start=null
lc test [partial-slug]
```
- Runs: python3 -m pytest <dir>/tests.py
- Prints results; exits non-zero if tests fail or errors occur

### remove
Remove a problem and its workspace.

Usage:
```bash path=null start=null
lc remove [partial-slug]
```
- Deletes the problem directory and removes it from problems.json
- Regenerates README to reflect the change

### publish
Mark a problem as published and update README. Prompts to add tags and pulls notes from notes.md.

Usage:
```bash path=null start=null
lc publish <slug>
# or publish all unpublished
lc publish --all
```
- Sets published=true, attaches notes and tags, updates README and problems.json

### unpublish
Unpublish a problem (clears notes and tags, removes from README listing).

Usage:
```bash path=null start=null
lc unpublish <slug>
```
- Sets published=false, clears notes/tags, updates README and problems.json

### generate-readme
Regenerate the top-level README from current published problems.

Usage:
```bash path=null start=null
lc generate-readme
```

## Notes
- The README shows only published problems and sorts them by difficulty.
- Fuzzy selection uses InquirerPy; spinners use yaspin.
- The scraper opens LeetCode in headless Chromium and extracts the Python3 starter.
- Tags and notes are stored in problems.json and rendered into the README when published.
