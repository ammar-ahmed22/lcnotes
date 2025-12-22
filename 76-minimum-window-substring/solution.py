class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        freq = {}
        for c in t:
            freq[c] = freq[c] + 1 if c in freq else 1


        l, r = 0, len(t) - 1

        for i in range(len(t)):
            if s[i] in freq:
                freq[s[i]] -= 1
        min_window = ""
        while r < len(s):
            is_valid = all(freq[c] <= 0 for c in freq)
            if is_valid:
                curr_window = r - l + 1
                if min_window == "" or curr_window < len(min_window):
                    min_window = s[l:r+1]

                # only slide once we get to minimum length
                if curr_window == len(t):
                    r += 1
                    if r < len(s) and s[r] in freq:
                        freq[s[r]] -= 1
                    
                # reduce window (always look for better)
                if s[l] in freq:
                    freq[s[l]] += 1
                l += 1
            else:
                r += 1
                if r < len(s) and s[r] in freq:
                    freq[s[r]] -= 1
                pass
        
        return min_window
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
