class Solution:

    def encode(self, strs: List[str]) -> str:
        master_string = "" 
        for string in strs:
            master_string += str(len(string)) + "/" + string
        return master_string

    def decode(self, s: str) -> List[str]:
        string_array = []
        i = 0
        while i < len(s):
            slash_index = s.find("/", i)
            length = int(s[i:slash_index])
            string_array.append(s[slash_index + 1 : slash_index + 1 + length])
            i = slash_index + 1 + length
        return string_array
