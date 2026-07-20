class Solution:

    def encode(self, strs: List[str]) -> str:
        # First, let's encode all the strs to hex. This ensures 
        # that there will be no issues using character delimiters 
        for idx, s in enumerate(strs):
            strs[idx] = s.encode("utf-8").hex() 

        # Then join with a delimiter
        return "#".join(strs) if len(strs) > 0 else "EMPTY"

    def decode(self, s: str) -> List[str]:
        if(s == "EMPTY"):
            return []

        # Split on the delimiter 
        tokenized: list[str] = s.split("#")

        # decode each of the strs 
        for idx, str_ in enumerate(tokenized):
            tokenized[idx] = bytes.fromhex(str_).decode("utf-8")
        
        return tokenized
        
