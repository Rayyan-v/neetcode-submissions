class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer=0
        end_pointer=len(numbers)-1
        found=False
        
        while found==False:
            sum=numbers[start_pointer]+numbers[end_pointer]
            if sum==target:
                found=True
            elif sum>target:
                end_pointer-=1
            elif sum<target:
                start_pointer+=1
        
        return [start_pointer+1, end_pointer+1]

            
            