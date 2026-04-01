class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "00"
        empty = ""
        for s in strs:
            empty = empty + s.encode().hex() + ","
        return empty[:-1]
    def decode(self, s: str) -> List[str]:
        if s == "00":
            return []
        string_list = s.split(",")
        for i in range(len(string_list)):
            string_list[i] = bytes.fromhex(string_list[i]).decode('utf-8')

        
        return string_list
        