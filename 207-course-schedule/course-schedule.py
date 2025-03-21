class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)} 
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        print(adj_list)
        
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if adj_list[course] == []:
                return True

            visitSet.add(course)
            for neighbor in adj_list[course]:
                if not dfs(neighbor): return False 

            visitSet.remove(course)
            adj_list[course] = []
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True 


