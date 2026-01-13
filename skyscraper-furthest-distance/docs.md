# Skyscraper Furthest Distance
A player needs to traverse between skyscrapers, carrying `springs` and `sandbags`. The `heights` of these buildings vary.

If the next building's rooftop is lower than or equal to the current one, the player can move freely.

If the next rooftop is higher, the player must either:

- Use `sandbags` (each sandbag increases the player's height by 1; if the sum of the current height and sandbags equals the next rooftop's height, the player can move forward).

- Use `springs` to jump directly to the next rooftop, regardless of height difference.

The goal is to determine the index of how far the player can travel.

**Example 1:**
```
Input: heights = [2, 3, 5, 1, 7], springs = 1, sandbags = 2
Output: 3
Explanation: Use 1 sandbag to move from 2 -> 3, use 1 spring to move from 3 -> 5, 5 -> 1 is a free move. Cannot move further, therefore, index 3.
```

**Example 2:**
```
Input: heights = [4, 2, 2, 6, 3, 7], springs = 1, sandbags = 4
Output: 5
Explanation: 4 -> 2 free, 2 -> 2 free, 2 -> 6 use 4 sandbags, 6 -> 3 free, 3 -> 7, need 4 sandbags, use spring. Can also use spring at 2 -> 6 instead, same result
```

**Example 3:**
```
Input: heights = [1, 5, 2, 3, 10], springs = 1, sandbags = 3
Output: 3
Explanation: 1 -> 5 must use spring, 5 -> 2 free, 2 -> 3 use 1 sandbag, 3 -> 10 need 7 sandbags or 1 spring, don't have either, return 3
```
