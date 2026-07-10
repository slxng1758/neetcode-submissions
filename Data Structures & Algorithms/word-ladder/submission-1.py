class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wmap = defaultdict(list)
        if endWord not in wordList:
            return 0
    
        for word in wordList:
            for j in range(len(word)):
                pat = word[:j]+"*"+word[j+1:]
                wmap[pat].append(word)
        vis = set([beginWord])
        steps = 1
        q = deque([beginWord])
        while q:
            sz = len(q)
            for i in range(sz):
                word = q.popleft()
                if word == endWord:
                    return steps
                for j in range(len(word)):
                    pat = word[:j]+"*"+word[j+1:]
                    for nword in wmap[pat]:
                        if nword not in vis:
                            vis.add(nword)
                            q.append(nword)
            steps+=1

        return 0