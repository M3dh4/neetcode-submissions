class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            graph[crs].append(preq)
        visit=set()
        cycle=set()
        output=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for p in graph[crs]:
                if not dfs(p):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output



        