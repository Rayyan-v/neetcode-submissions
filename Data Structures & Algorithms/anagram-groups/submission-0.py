class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for word in strs:
            count = [0]*26
            for char in word:
                index=ord(char)-ord('a')
                count[index]+=1
            
            signature = tuple(count)
            if signature in hash_table:
                hash_table[signature].append(word)
            else:
                hash_table[signature] = [word]

        output = []
        for signature in hash_table:
            output.append(hash_table[signature])

        return output