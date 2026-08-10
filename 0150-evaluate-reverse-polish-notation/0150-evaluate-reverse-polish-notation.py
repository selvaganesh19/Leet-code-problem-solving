class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for c in tokens:
            if c == "+" :
                s.append(s.pop()+s.pop())
            elif c == "-":
                b,a = s.pop(), s.pop()
                s.append(a-b)
            elif c == "*":
                s.append(s.pop()*s.pop())
            elif c == "/":
                b, a = s.pop(), s.pop()
                s.append(int(a / b))

            else:
                s.append(int(c))
        
        return s[-1]
