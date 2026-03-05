# dfs.py

from generator import generate_successors


def dfs(state, goal, visited, path):
    if state == goal:
        return path

    visited.add(state)

    for successor in generate_successors(state):
        if successor not in visited:
            result = dfs(successor, goal, visited, path + [successor])
            if result is not None:
                return result

    return None


if __name__ == "__main__":
    start = (0, 0, 0)   # all on RIGHT
    goal = (3, 3, 1)    # all on LEFT

    visited = set()
    solution = dfs(start, goal, visited, [start])

    if solution:
        for step in solution:
            print(step)
        print("steps:", len(solution) - 1)
    else:
        print("no solution found")