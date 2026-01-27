class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            indegree[pre] += 1
            adj_list[course].append(pre)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        return finish == numCourses

