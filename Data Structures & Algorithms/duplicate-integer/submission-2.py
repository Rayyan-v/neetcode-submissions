class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hashset = set()

        for num in nums:
            if num in nums_hashset:
                return True
            
            nums_hashset.add(num)
        
        return False
        