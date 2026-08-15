class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        for course,preq in prerequisites:
            graph[course].append(preq)
        
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if graph[course]==[]:
                return True
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            graph[course]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
