class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False
            if adj_list[course] == []:
                return True

            visitSet.add(course)
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
            adj_list[course] = []
            visitSet.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True