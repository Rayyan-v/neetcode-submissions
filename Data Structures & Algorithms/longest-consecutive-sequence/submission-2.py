class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #validate pairs of numbers that are exactly one less than the other
        nums.sort()
        consecutive_count=0
        consecutive_counts=[]
        print(nums)
        for i in range(len(nums)):
            if i==0:
                consecutive_count+=1
            if i>0:
                if nums[i]==(nums[i-1]+1) and consecutive_count>0:
                    consecutive_count+=1
                elif nums[i]==(nums[i-1]+1):
                    consecutive_count=1
                    consecutive_count+=1
                elif nums[i]==nums[i-1]:
                    continue
                else:
                    consecutive_counts.append(consecutive_count)
                    consecutive_count=0
        consecutive_counts.append(consecutive_count)

        
        highest_consecutive_count=0
        print(consecutive_counts)
        for j in range(len(consecutive_counts)):
            if consecutive_counts[j]>highest_consecutive_count:
                highest_consecutive_count=consecutive_counts[j]
        
        return highest_consecutive_count

                