class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        output = []
        visited, incycle = set(), set()

        def dfs(course):
            if course in incycle:
                return False
            if course in visited:
                return True

            incycle.add(course)
            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
            incycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output