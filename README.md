<div align="center">
    <h1>lcnotes</h1>
    <p>CLI to create dedicated Python environments and run/test Leetcode problems with documentation</p>
    <p>
      <img src="https://img.shields.io/badge/17-easy-green" />
      <img src="https://img.shields.io/badge/35-medium-yellow" />
      <img src="https://img.shields.io/badge/7-hard-red" />
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
| :-----: | :---: | :--------: | :------: |
| [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram) | [notes](./84-largest-rectangle-in-histogram/notes.md) | ![Static Badge](https://img.shields.io/badge/Hard-red?style=flat) | [solution](./84-largest-rectangle-in-histogram/solution.py)
| [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring) | [notes](./76-minimum-window-substring/notes.md) | ![Static Badge](https://img.shields.io/badge/Hard-red?style=flat) | [solution](./76-minimum-window-substring/solution.py)
| [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water) | [notes](./42-trapping-rain-water/notes.md) | ![Static Badge](https://img.shields.io/badge/Hard-red?style=flat) | [solution](./42-trapping-rain-water/solution.py)
| [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum) | [notes](./239-sliding-window-maximum/notes.md) | ![Static Badge](https://img.shields.io/badge/Hard-red?style=flat) | [solution](./239-sliding-window-maximum/solution.py)
| [Max Level Party Invites](https://leetcode.com/problems/max-level-party-invites) | [notes](./max-level-party-invites/notes.md) | ![Static Badge](https://img.shields.io/badge/Hard-red?style=flat) | [solution](./max-level-party-invites/solution.py)
| [Rummy Card Game](https://leetcode.com/problems/rummy-card-game) | [notes](./rummy-card-game/notes.md) | ![Static Badge](https://img.shields.io/badge/Hard-red?style=flat) | [solution](./rummy-card-game/solution.py)
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) | [notes](./23-merge-k-sorted-lists/notes.md) | ![Static Badge](https://img.shields.io/badge/Hard-red?style=flat) | [solution](./23-merge-k-sorted-lists/solution.py)
| [49. Group Anagrams](https://leetcode.com/problems/group-anagrams) | [notes](./49-group-anagrams/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./49-group-anagrams/solution.py)
| [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements) | [notes](./347-top-k-frequent-elements/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./347-top-k-frequent-elements/solution.py)
| [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) | [notes](./238-product-of-array-except-self/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./238-product-of-array-except-self/solution.py)
| [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku) | [notes](./36-valid-sudoku/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./36-valid-sudoku/solution.py)
| [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence) | [notes](./128-longest-consecutive-sequence/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./128-longest-consecutive-sequence/solution.py)
| [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) | [notes](./167-two-sum-ii-input-array-is-sorted/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./167-two-sum-ii-input-array-is-sorted/solution.py)
| [15. 3Sum](https://leetcode.com/problems/3sum) | [notes](./15-3sum/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./15-3sum/solution.py)
| [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water) | [notes](./11-container-with-most-water/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./11-container-with-most-water/solution.py)
| [155. Min Stack](https://leetcode.com/problems/min-stack) | [notes](./155-min-stack/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./155-min-stack/solution.py)
| [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation) | [notes](./150-evaluate-reverse-polish-notation/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./150-evaluate-reverse-polish-notation/solution.py)
| [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | [notes](./22-generate-parentheses/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./22-generate-parentheses/solution.py)
| [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures) | [notes](./739-daily-temperatures/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./739-daily-temperatures/solution.py)
| [853. Car Fleet](https://leetcode.com/problems/car-fleet) | [notes](./853-car-fleet/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./853-car-fleet/solution.py)
| [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix) | [notes](./74-search-a-2d-matrix/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./74-search-a-2d-matrix/solution.py)
| [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas) | [notes](./875-koko-eating-bananas/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./875-koko-eating-bananas/solution.py)
| [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) | [notes](./153-find-minimum-in-rotated-sorted-array/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./153-find-minimum-in-rotated-sorted-array/solution.py)
| [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) | [notes](./33-search-in-rotated-sorted-array/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./33-search-in-rotated-sorted-array/solution.py)
| [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | [notes](./3-longest-substring-without-repeating-characters/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./3-longest-substring-without-repeating-characters/solution.py)
| [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement) | [notes](./424-longest-repeating-character-replacement/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./424-longest-repeating-character-replacement/solution.py)
| [567. Permutation in String](https://leetcode.com/problems/permutation-in-string) | [notes](./567-permutation-in-string/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./567-permutation-in-string/solution.py)
| [143. Reorder List](https://leetcode.com/problems/reorder-list) | [notes](./143-reorder-list/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./143-reorder-list/solution.py)
| [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | [notes](./19-remove-nth-node-from-end-of-list/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./19-remove-nth-node-from-end-of-list/solution.py)
| [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | [notes](./2-add-two-numbers/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./2-add-two-numbers/solution.py)
| [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number) | [notes](./287-find-the-duplicate-number/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./287-find-the-duplicate-number/solution.py)
| [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree) | [notes](./235-lowest-common-ancestor-of-a-binary-search-tree/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./235-lowest-common-ancestor-of-a-binary-search-tree/solution.py)
| [Minimum Lock Turns](https://leetcode.com/problems/minimum-lock-turns) | [notes](./minimum-lock-turns/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./minimum-lock-turns/solution.py)
| [Skyscraper Furthest Distance](https://leetcode.com/problems/skyscraper-furthest-distance) | [notes](./skyscraper-furthest-distance/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./skyscraper-furthest-distance/solution.py)
| [752. Open the Lock](https://leetcode.com/problems/open-the-lock) | [notes](./752-open-the-lock/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./752-open-the-lock/solution.py)
| [1642. Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach) | [notes](./1642-furthest-building-you-can-reach/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./1642-furthest-building-you-can-reach/solution.py)
| [1730. Shortest Path To Get Food](https://leetcode.com/problems/1730-shortest-path-to-get-food) | [notes](./1730-shortest-path-to-get-food/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./1730-shortest-path-to-get-food/solution.py)
| [Infinite Taxi Driver](https://leetcode.com/problems/infinite-taxi-driver) | [notes](./infinite-taxi-driver/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./infinite-taxi-driver/solution.py)
| [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence) | [notes](./334-increasing-triplet-subsequence/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./334-increasing-triplet-subsequence/solution.py)
| [443. String Compression](https://leetcode.com/problems/string-compression) | [notes](./443-string-compression/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./443-string-compression/solution.py)
| [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer) | [notes](./138-copy-list-with-random-pointer/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./138-copy-list-with-random-pointer/solution.py)
| [146. LRU Cache](https://leetcode.com/problems/lru-cache) | [notes](./146-lru-cache/notes.md) | ![Static Badge](https://img.shields.io/badge/Medium-orange?style=flat) | [solution](./146-lru-cache/solution.py)
| [1. Two Sum](https://leetcode.com/problems/two-sum) | [notes](./1-two-sum/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./1-two-sum/solution.py)
| [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate) | [notes](./217-contains-duplicate/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./217-contains-duplicate/solution.py)
| [242. Valid Anagram](https://leetcode.com/problems/valid-anagram) | [notes](./242-valid-anagram/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./242-valid-anagram/solution.py)
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome) | [notes](./125-valid-palindrome/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./125-valid-palindrome/solution.py)
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | [notes](./20-valid-parentheses/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./20-valid-parentheses/solution.py)
| [704. Binary Search](https://leetcode.com/problems/binary-search) | [notes](./704-binary-search/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./704-binary-search/solution.py)
| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | [notes](./121-best-time-to-buy-and-sell-stock/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./121-best-time-to-buy-and-sell-stock/solution.py)
| [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) | [notes](./206-reverse-linked-list/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./206-reverse-linked-list/solution.py)
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) | [notes](./21-merge-two-sorted-lists/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./21-merge-two-sorted-lists/solution.py)
| [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle) | [notes](./141-linked-list-cycle/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./141-linked-list-cycle/solution.py)
| [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree) | [notes](./226-invert-binary-tree/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./226-invert-binary-tree/solution.py)
| [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) | [notes](./104-maximum-depth-of-binary-tree/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./104-maximum-depth-of-binary-tree/solution.py)
| [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree) | [notes](./543-diameter-of-binary-tree/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./543-diameter-of-binary-tree/solution.py)
| [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree) | [notes](./110-balanced-binary-tree/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./110-balanced-binary-tree/solution.py)
| [100. Same Tree](https://leetcode.com/problems/same-tree) | [notes](./100-same-tree/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./100-same-tree/solution.py)
| [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree) | [notes](./572-subtree-of-another-tree/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./572-subtree-of-another-tree/solution.py)
| [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately) | [notes](./1768-merge-strings-alternately/notes.md) | ![Static Badge](https://img.shields.io/badge/Easy-green?style=flat) | [solution](./1768-merge-strings-alternately/solution.py)
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
