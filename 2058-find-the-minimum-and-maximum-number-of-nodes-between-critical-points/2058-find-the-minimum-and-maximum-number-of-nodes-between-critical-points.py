
class Solution:
    def nodesBetweenCriticalPoints(self, head: 'Optional[ListNode]') -> list[int]:
        first_idx = -1      
        last_idx = -1       
        min_dist = float('inf')

        prev = head
        curr = head.next
        idx = 1              
        while curr.next is not None:
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val

            if is_max or is_min:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - last_idx)
                last_idx = idx

            prev = curr
            curr = curr.next
            idx += 1

        if first_idx == last_idx:  
            return [-1, -1]

        max_dist = last_idx - first_idx
        return [min_dist, max_dist]