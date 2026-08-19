class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        
        LEFT   = 0b00001111   
        MIDDLE = 0b00111100  
        RIGHT  = 0b11110000  

        row_masks: dict[int, int] = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                bit = 1 << (seat - 2)
                row_masks[row] = row_masks.get(row, 0) | bit

        total = 0
        for mask in row_masks.values():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                total += 2
            elif (mask & LEFT) == 0 or (mask & RIGHT) == 0 or (mask & MIDDLE) == 0:
                total += 1
      
        total += 2 * (n - len(row_masks))

        return total