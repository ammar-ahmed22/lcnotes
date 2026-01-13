from typing import List, Tuple, Dict
from collections import defaultdict

class Solution:
    def maxLevelPartyInvites(self, levels: List[int], reporting_chain: List[List[int]]) -> int:
        n = len(levels)
        children = defaultdict(list)
        # Create adjacency list and mark parents to extract roots later
        has_parent = [False] * n
        for manager, report in reporting_chain:
            children[manager].append(report)
            has_parent[report] = True


        dp: Dict[int, Tuple[int, int]] = {}
        def dfs(u: int) -> Tuple[int, int]:
            if u in dp:
                return dp[u]

            invite_u = levels[u]
            skip_u = 0
            for v in children[u]:
                invite_v, skip_v = dfs(v)
                invite_u += skip_v # if u is invited, sum if v is not invited (skip_v)
                skip_u += max(invite_v, skip_v) # if u is skipped, we can choose to invite v or not

            dp[u] = (invite_u, skip_u)
            return dp[u]

        # Only start DFS on roots because otherwise we can miss nodes or double count them
        roots = [i for i in range(n) if not has_parent[i]]
        total = 0
        for u in roots:
            invite, skip = dfs(u)
            total += max(invite, skip)
        return total;

if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
