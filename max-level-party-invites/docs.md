# Max Level Party Invites
You are given a list of `n` employees each assigned a level between 0 and 10.
The employees and their levels are represented as an array of integers, `levels`, where the index, `i`, is the employee's identifier and the value `levels[i]` is their level.

You are also provided a `reporting_chain` which represents the reporting structure of employees where each entries first value is the manager and the second value in that entry is their direct report.

For example, a `reporting_chain` that consists of `[[0, 1], [0, 2], [1, 3]]` would indicate:

Employee 0 manages Employee 1
Employee 0 manages Employee 2
Employee 1 manages Employee 3

You are tasked with inviting people from this company to a party, however, the constraint is the if an employee is invited, none of their direct reports can be invited.

Following this constraint, return the max sum of levels possible given a selection of employees to invite.

**Example 1:**

```
Input: levels = [10, 9, 9, 5, 5, 5, 6], reporting_chain = [[0, 1], [0,2], [1, 3], [1, 4], [1, 5], [2, 6]]
Output: 31
Explanation: If we invite 0 (level 10), employee 1 (level 9) and 2 (level 9) cannot be invited. Inviting the rest is fine and thus the best sum is 31.
```

**Example 2:**

```
Input: levels = [8, 6, 7, 4, 5], reporting_chain = [[0, 1], [1, 2], [2, 3], [3, 4]]
Output: 20
Explanation: Invite 0, 2, 4. Skip 1, 3.
```

**Example 3:**

```
Input: levels = [10, 9], reporting_chain = [[0, 1]]
Output: 10
Explanation: No other employees
```

