class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i in range(len(heights)):
            ch = heights[i]
            idx = i
            while stack and ch<stack[-1][1]:
                maxArea = max(maxArea, (i-stack[-1][0])*stack[-1][1])
                idx = stack[-1][0]
                stack.pop()
            if not stack:
                idx = 0
            elif ch==stack[-1][1]:
                ind, hei = stack[-1]
                idx = ind
            stack.append((idx,ch))
        
        n = len(heights)
        while stack:
            ind, hei = stack[-1]
            maxArea = max(maxArea, (n-ind)*hei)
            stack.pop()
        return maxArea

        