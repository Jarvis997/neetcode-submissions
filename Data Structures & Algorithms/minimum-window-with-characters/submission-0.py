class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
            
        # 1. Count character frequencies required by string t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
            
        # Map to track character frequencies in our active window
        window_count = {}
        
        # 'need' is the number of unique characters in t we must satisfy
        have, need = 0, len(t_count)
        
        # Record the best window found: [length, left_index, right_index]
        res = [float("inf"), 0, 0]
        left = 0
        
        # 2. Expand the window using the right pointer
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If a character matches the exact frequency requirement from t, increment 'have'
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
                
            # 3. Contraction Phase: Shrink the window while it remains valid
            while have == need:
                # Update our result if the current window is smaller than our record
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left, right]
                    
                # The character leaving the window from the left
                left_char = s[left]
                window_count[left_char] -= 1
                
                # If removing this character breaks our criteria, decrement 'have'
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                    
                left += 1  # Move left pointer forward
                
        # Return the slice if a valid window was found, otherwise return ""
        return s[res[1]:res[2] + 1] if res[0] != float("inf") else ""