class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find max width and find max height
        #max width is found by subtracting the biggest from smallest
        #max height is maximum shared number between the 2 indices min(x, y)
        start_pointer=0
        end_pointer=len(heights)-1
        highest_area=0
        for j in range(len(heights)):
            width=end_pointer-start_pointer
            height=min(heights[end_pointer], heights[start_pointer])
            area=width*height
            
            if heights[end_pointer]>=heights[start_pointer]:
                start_pointer+=1
            elif heights[end_pointer]<heights[start_pointer]:
                end_pointer-=1
            
            if area>highest_area:
                highest_area=area
        
        return highest_area

        
