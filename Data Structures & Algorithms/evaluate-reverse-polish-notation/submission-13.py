class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if self.is_number(i):
                stack.append(i)
            else:
                evaluated = int(eval(stack.pop(-2) +  i + stack.pop(-1)))
                stack.append(str(evaluated))
                
                
        return evaluated

    def is_number(self, s):
        try:
            float(s) # or int(s) if only integers are allowed
            return True
        except ValueError:
            return False