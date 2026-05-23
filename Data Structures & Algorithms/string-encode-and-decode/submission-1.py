class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            
            # FIXED: We MUST extract the number before we can use 'length'!
            length = int(s[i:j])
            
            # Slice the word and append it
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # FIXED: Added the missing 'h' to length
            i = j + 1 + length

        return res