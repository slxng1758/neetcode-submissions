class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subs = []
        candidates.sort()
        def dfs(i, csum):
            if csum == target:
                res.append(subs.copy())
                return
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if csum + candidates[j]>target:
                    return
                subs.append(candidates[j])
                dfs(j+1, csum+candidates[j])
                subs.pop()
        dfs(0,0)
        return res