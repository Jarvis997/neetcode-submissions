class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # Format: length + '#' + string
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter '#' starting from position i
            j = i
            while s[j] != '#':
                j += 1
                
            # 2. Extract and parse the length of the string
            length = int(s[i:j])
            
            # 3. Slice out the exact string using the parsed length
            start_of_str = j + 1
            end_of_str = start_of_str + length
            decoded_strs.append(s[start_of_str:end_of_str])
            
            # 4. Move the pointer to the start of the next encoded segment
            i = end_of_str
            
        return decoded_strs