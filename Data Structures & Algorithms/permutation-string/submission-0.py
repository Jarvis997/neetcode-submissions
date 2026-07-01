class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Initialize frequency arrays for 26 lowercase English letters
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # 1. Populate s1 frequencies and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # 2. If the very first window is a match, we are done
        if s1_count == window_count:
            return True
            
        # 3. Slide the window across the rest of s2
        for i in range(len(s1), len(s2)):
            # Add the new character entering the window from the right
            incoming_char = s2[i]
            window_count[ord(incoming_char) - ord('a')] += 1
            
            # Remove the old character leaving the window from the left
            outgoing_char = s2[i - len(s1)]
            window_count[ord(outgoing_char) - ord('a')] -= 1
            
            # Check if the updated window matches s1's character profile
            if s1_count == window_count:
                return True
                
        return False