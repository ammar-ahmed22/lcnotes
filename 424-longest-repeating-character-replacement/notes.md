## Intuition
In any window, the minimum replacements needed equals `window_length - max_frequency_of_any_char`. If this exceeds k, shrink the window. Otherwise, we have a valid window where we can make all characters the same.

## Implementation
Maintain a frequency array for 26 characters and track the maximum frequency seen. For each right pointer position, increment the character's frequency and update max frequency. If `window_size - max_freq > k`, the window is invalid—shrink from the left by decrementing that character's frequency and moving `l`. Track the maximum valid window length.

## Edge-cases
Window size is `r - l + 1`. The max frequency doesn't need to decrease when shrinking—if it was valid before, using that max won't make the window smaller than it could be.

## Complexity
- Time: `O(n)` — each character processed once
- Space: `O(1)` — frequency array is fixed at 26 elements
