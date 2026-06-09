class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        for c in tokens:
                if c =='*':
                    firs = numstack.pop()
                    sec = numstack.pop()
                    val=firs*sec
                    numstack.append(int(val))
                elif c =='+':
                    firs = numstack.pop()
                    sec = numstack.pop()
                    val=firs+sec
                    numstack.append(int(val))
                elif c =='-':
                    firs = numstack.pop()
                    sec = numstack.pop()
                    val=sec-firs
                    numstack.append(int(val))
                elif c =='/':
                    firs = numstack.pop()
                    sec = numstack.pop()
                    val=(sec)/firs
                    numstack.append(int(val))
                else:
                    numstack.append(int(c))
        return int(numstack[-1])



        