from typing import List, Tuple, Dict
from collections import defaultdict

class Solution:
    def maxLevelPartyInvites(self, levels: List[int], reporting_chain: List[List[int]]) -> int:
        n = len(levels)
        reports = defaultdict(list)
        # Create adjacency list and mark parents to extract roots later
        has_parent = [False] * n
        for manager, report in reporting_chain:
            reports[manager].append(report)
            has_parent[report] = True


        memo: Dict[int, Tuple[int, int]] = {}
        def dfs(employee: int) -> Tuple[int, int]:
            if employee in memo:
                return memo[employee]

            invite_employee = levels[employee]
            skip_employee = 0
            for report in reports[employee]:
                invite_report, skip_report = dfs(report)
                invite_employee += skip_report # if u is invited, sum if v is not invited (skip_v)
                skip_employee += max(invite_report, skip_report) # if u is skipped, we can choose to invite v or not

            memo[employee] = (invite_employee, skip_employee)
            return memo[employee]

        # Only start DFS on roots because otherwise we can miss nodes or double count them
        root_employees = [i for i in range(n) if not has_parent[i]]
        total = 0
        for root_employee in root_employees:
            invite, skip = dfs(root_employee)
            total += max(invite, skip)
        return total;

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
