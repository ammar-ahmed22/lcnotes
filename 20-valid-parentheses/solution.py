
class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "(": ")",
            "{": "}",
            "[": ']',
        }
        stack = []
        for c in s:
            if c in map:
                # opening bracket
                stack.append(map[c])
            else:
                if len(stack) == 0 or stack[-1] != c:
                    return False
                stack.pop()


        return len(stack) == 0
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
