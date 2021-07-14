from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        
        def createGraph():

            graph = defaultdict(list)

            for i in range(len(equations)):

                a, b = equations[i]
                cost = values[i]

                graph[a].append((b, cost))
                graph[b].append((a, 1/cost))

            return graph

        def bfs(start, end, graph):

            q = deque([(start, 1)])
            seen = set({start})

            while q:

                curr_node, val = q.popleft()

                if curr_node == end:
                    return val

                for nei, cost in graph[curr_node]:

                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, val * cost))

            return -1

        graph = createGraph()
        ans = []

        for s, e in queries:

            if s not in graph or e not in graph:
                ans.append(-1)
            else:
                ans.append(bfs(s, e, graph))

        return ans


test = Solution()

a = [["a","b"],["b","c"]]
b = [2.0,3.0]
c = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(test.calcEquation(a,b,c))
        
            
        
        
        