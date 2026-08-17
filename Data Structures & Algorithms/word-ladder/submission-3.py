from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        
        visit=set()
        q=deque()
        visit.add(beginWord)
        q.append(beginWord)
        count=1
        while q:
            for _ in range(len(q)):
                word= q.popleft()
                if word==endWord:
                    return count
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neiw in nei[pattern]:
                        if neiw not in visit:
                            visit.add(neiw)
                            q.append(neiw)
            count+=1
        return 0
        