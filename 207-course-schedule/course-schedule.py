# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         adj_list = { i:[] for i in range(numCourses) }
#         for course, pre in prerequisites:
#             adj_list[course].append(pre)
        
#         visitSet = set()

#         def dfs(course):
#             if course in visitSet:
#                 return False
#             if adj_list[course] == []:
#                 return True
            
#             visitSet.add(course)
#             for pre in adj_list[course]:
#                 if not dfs(pre):
#                     return False
#             visitSet.remove(course)
#             adj_list[course] == []
#             return True

#         for course in range(numCourses):
#             if not dfs(course):
#                 return False
#         return True 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True