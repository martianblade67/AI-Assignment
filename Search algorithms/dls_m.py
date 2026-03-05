# dls.py

from generator import generate_successors


def dls(state, goal, limit, visited, path):
    if state == goal:
        return path

    if limit == 0:
        return None

    visited.add(state)

    for successor in generate_successors(state):
        if successor not in visited:
            result = dls(successor, goal, limit - 1, visited, path + [successor])
            if result is not None:
                return result

    return None


if __name__ == "__main__":
    start = (0, 0, 0)
    goal = (3, 3, 1)

    depth_limit = 10

    visited = set()
    solution = dls(start, goal, depth_limit, visited, [start])

    if solution:
        for step in solution:
            print(step)
        print("steps:", len(solution) - 1)
    else:
        print("no solution within depth limit")