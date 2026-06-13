class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        slist = sorted(pairs, reverse = True)
        stack = []
        for pos, sp in slist:
            tim = (target-pos)/sp
            stack.append(tim)
            if len(stack)>1 and tim<=stack[-2]:
                stack.pop()
        print(slist)
        return len(stack)


