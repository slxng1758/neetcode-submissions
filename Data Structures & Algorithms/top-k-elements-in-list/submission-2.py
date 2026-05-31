class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(nums)):
            map[nums[i]] += 1
        print(map)

        fm = defaultdict(list)
        for ke, v in map.items():
            fm[v].append(ke)
        print(fm)

        ls = []
        for i in range(len(nums), 0, -1):
            for n in fm[i]:
                ls.append(n)
                if len(ls) == k:
                    return ls
            
        