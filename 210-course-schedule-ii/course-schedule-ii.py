class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj_list =[[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            indegree[pre] += 1
            adj_list[course].append(pre)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finish = 0
        output = []
        while q:
            node = q.popleft();
            output.append(node)
            finish += 1
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        if finish != numCourses:
            return []
        return output[::-1]