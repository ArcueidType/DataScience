import numpy as np

status = {0: '人羊狼菜', 1: '人狼菜', 2: '人羊狼', 3: '人羊菜', 4: '人羊',
          5: '狼菜', 6: '狼', 7: '菜', 8: '羊', 9:'空'}

graph = {0: [5], 1: [5, 6, 7], 2: [6, 8], 3: [7, 8], 4: [8, 9],
         5: [0, 1], 6:[1, 2], 7:[1, 3], 8:[2, 3, 4], 9: [4]}

tag = np.array([0 for i in range(10)])


def dfs(graph: dict, start: int, path: list):
    path.append(status[start])
    currPath = path.copy()
    if start == 9:
        return [path]

    pathsResult = []
    for node in graph[start]:
        if status[node] not in path:
            paths = dfs(graph, node, path)
            for p in paths:
                pathsResult.append(p)
            path = currPath.copy()
    return pathsResult

paths = dfs(graph, 0, [])
for path in paths:
    print(path)
            
                