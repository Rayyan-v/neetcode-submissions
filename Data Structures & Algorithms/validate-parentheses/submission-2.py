class Solution:
    def isValid(self, s: str) -> bool:
        valid_combos={'}':'{', ')':'(', ']':'['}
        stack=[]
        for i in range(len(s)):
            if s[i] in valid_combos and stack:
                if stack[-1]==valid_combos[s[i]]:
                    stack.pop()
                else:
                    print(stack[-1], s[i], valid_combos[s[i]])
                    return False
            else:
                stack.append(s[i])

        if len(stack)==0:
            return True
        return False
        
                
