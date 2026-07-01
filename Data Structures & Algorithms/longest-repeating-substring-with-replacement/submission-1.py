class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Tracks character frequencies in the current window
        max_len = 0
        max_freq = 0 # Tracks the highest frequency of any single character seen in the window
        left = 0
        
        for right in range(len(s)):
            # 1. Add the incoming character to our frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. Update the maximum frequency found in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # 3. If the number of characters to replace exceeds k, shrink the window
            window_len = right - left + 1
            if window_len - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # 4. Recalculate window length after potential shrinkage and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len