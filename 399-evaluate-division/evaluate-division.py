class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = set()
        for i, eq in enumerate(equations):
            l1 = eq[0]
            l2 = eq[1]
            nodes.add(l1) 
            nodes.add(l2)
        
        length = len(nodes)
        nodes = list(nodes)
        nodes.sort()
        nodes_map = {node:i for i,node in enumerate(nodes)}
        adj_matrix = [[0]*length for i in range(length)]
        for i in range(length):
            adj_matrix[i][i] = 1


        for i,eq in enumerate(equations):
            value = values[i]
            adj_matrix[nodes_map[eq[0]]][nodes_map[eq[1]]] = value
            adj_matrix[nodes_map[eq[1]]][nodes_map[eq[0]]] = 1/value

        answer = [0]*len(queries)
        for i in range(len(queries)):
            visited = [False for i in range(len(nodes))] 
            if queries[i][0] not in nodes or queries[i][1] not in nodes:
                answer[i] = -1
                continue

            source_index = nodes_map[queries[i][0]]
            target_index = nodes_map[queries[i][1]]
            if source_index == target_index:
                answer[i] = 1
                continue

            val = 1
            val = self.recursive(source_index, target_index, visited, adj_matrix, val)
            answer[i] = val
        return answer 

    def recursive(self, source_index, target_index, visited, adj_matrix, val):
        visited[source_index] = True 
        neighbors = adj_matrix[source_index] 
        intermediate_val = -1
         
        for i,n in enumerate(neighbors):
            if n != 0 and visited[i] == False:
                if i == target_index:
                    intermediate_val = val * n
                    break
                else:
                    intermediate_val = self.recursive(i, target_index, visited, adj_matrix, val*n)
                    if intermediate_val != -1:
                        break
        return intermediate_val




            
        

        