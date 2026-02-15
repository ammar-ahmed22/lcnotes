## Intuition
In any window, the number of characters we need to replace equals the window length minus the count of the most frequent character. If this exceeds k, the window is invalid and must shrink.

## Implementation
Use a frequency array (26 elements) and track the maximum frequency seen. Expand the window right, updating frequencies. If `windowLength - maxFreq > k`, the window needs too many replacements—shrink from the left. Track the maximum valid window length.

## Edge-cases
Window size is `r - l + 1`. The maxFreq doesn't need to decrease when shrinking because we only care about finding larger valid windows, not maintaining exact counts.

## Complexity
Time `O(n)` for a single pass. Space `O(1)` since the frequency array is fixed at 26 elements.
