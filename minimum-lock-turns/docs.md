# Minimum Lock Turns
Given a starting lock combination (e.g. `0000`) find the minimum number of turns required for each wheel to get to a `target` (e.g. `0202`) in the presence of potentially `blocked` states.


**Example 1:**

```
Input: start = "0000", target = "0202", blocked = ["0201","0101","0102","1212","2002"]
Output: 6
```

**Example 2:**

```
Input: start = "1234", target = "1236", blocked = []
Output: 2
```

**Example 3:**

```
Input: start = "5555", target = "5559", blocked = ["5556", "5557", "5558"]
Output: 6
```



