class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create an array of 9 empty sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Calculate the unique 3x3 box index (0 to 8)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # If the number is already seen in this row, col, or box, it's invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # Otherwise, record the number in all three respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True