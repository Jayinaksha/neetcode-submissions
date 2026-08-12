import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        operations = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
        if len(tokens) > 1:
            for t in tokens:
                if t in operations:
                    a = stack.pop()
                    b = stack.pop()
                    ans = operations[t](int(b), int(a))
                    stack.append(ans)
                else:
                    stack.append(t)
            return int(stack[-1])
        else:
            return int(tokens[0])