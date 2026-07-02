class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Stores the most recent index of each character: { char: index }
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is a duplicate and exists inside our current window
            if current_char in char_map and char_map[current_char] >= left:
                # Shrink the window by jumping 'left' past the old duplicate
                left = char_map[current_char] + 1
            
            # Record/update the character's latest position
            char_map[current_char] = right
            
            # Calculate the current window size and check if it's a new record
            max_length = max(max_length, right - left + 1)
            
        return max_length