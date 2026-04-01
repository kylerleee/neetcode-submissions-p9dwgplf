class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {')':'(',
                         ']':'[',
                         '}':'{',
                        }
        open_bracket_list = []
        for bracket in s:
            if bracket in bracket_pairs.values():
                open_bracket_list.append(bracket)
            elif len(open_bracket_list) == 0 or bracket_pairs[bracket] != open_bracket_list[-1]:
                return False
            else:
                open_bracket_list.pop()

        if len(open_bracket_list) != 0:
            return False
        return True

   