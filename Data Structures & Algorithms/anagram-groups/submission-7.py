class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for itm in strs:
            ss = ''.join(sorted(itm))
            if ss not in map:
                map[ss] = []
            map[ss].append(itm)
        return list(map.values())