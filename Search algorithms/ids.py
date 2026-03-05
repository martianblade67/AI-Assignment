# ids.py

from dls_m import dls


def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        result = dls(start, goal, depth, visited, [start])
        if result is not None:
            return result
    return None


if __name__ == "__main__":
    start = (0, 0, 0)
    goal = (3, 3, 1)

    solution = ids(start, goal, 20)

    if solution:
        for step in solution:
            print(step)
        print("steps:", len(solution) - 1)
    else:
        print("no solution found")