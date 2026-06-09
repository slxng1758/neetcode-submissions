class Solution:
    def trap(self, height: List[int]) -> int:
        psa = [0]*len(height)
        ssa = [0]*len(height)
        psa[0] = height[0]
        ssa[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-1):
            psa[i+1] = max(psa[i],height[i+1])
        for i in range(len(height)-1, 0, -1):
            ssa[i-1] = max(ssa[i],height[i-1])
        print(psa)
        print(ssa)
        water = 0
        for i in range(len(height)):
            water += min(ssa[i],psa[i])-height[i]
        return water
            

        