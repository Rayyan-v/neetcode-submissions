class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products=[]
        prefix_product=1
        for i in range(0, len(nums)):
            if i>0:
                prefix_product*=nums[i-1]
            prefix_products.append(prefix_product)

        suffix_products=[]
        suffix_product=1
        for j in range(len(nums), 0, -1):
            if j < len(nums):
                suffix_product*=nums[j]
            suffix_products.append(suffix_product)
        suffix_products.reverse()
        
        outputs=[]
        for k in range(0, len(nums)):
            outputs.append(prefix_products[k]*suffix_products[k])
        return outputs

        
