class Solution:
    def isPalindrome(self, s: str) -> bool:
        spliced_copy=[]
        for char in s:
            if char.isalnum():
                spliced_copy.append(char.lower())
            else:
                continue
        
        reversed_spliced_copy=[]
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                reversed_spliced_copy.append(s[i].lower())
            else:
                continue
        
        print(reversed_spliced_copy, " ", spliced_copy)
        if reversed_spliced_copy==spliced_copy:
            return True
        return False