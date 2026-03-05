# bfs.py

from collections import deque
from generator import generate_successors


def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for successor in generate_successors(state):
            if successor not in visited:
                queue.append((successor, path + [successor]))

    return None


if __name__ == "__main__":
    start = (0, 0, 0)
    goal = (3, 3, 1)

    solution = bfs(start, goal)

    if solution:
        for step in solution:
            print(step)
        print("steps:", len(solution) - 1)
    else:
        print("no solution found")