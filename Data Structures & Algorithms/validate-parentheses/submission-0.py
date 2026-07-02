class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their matching opening brackets
        close_to_open = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is a closing bracket
            if char in close_to_open:
                # Pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the opening bracket doesn't match, it's invalid
                if close_to_open[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were properly matched
        return len(stack) == 0