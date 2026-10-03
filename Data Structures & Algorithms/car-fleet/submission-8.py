class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions and speeds, then sort closest to target first
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            
            # If the current car catches up to the fleet ahead of it, merge them
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        # The number of items left in the stack represents total fleets
        return len(stack)