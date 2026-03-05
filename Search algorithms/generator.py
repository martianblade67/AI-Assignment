
total_m = 3   
total_c = 3

# boat = 0 → right
# boat = 1 → left



moves = [
    (1, 0),   
    (2, 0),
    (0, 1),
    (0, 2),
    (1, 1)
]


def is_valid(m_left, c_left):
    if m_left < 0 or m_left > total_m:
        return False
    if c_left < 0 or c_left > total_c:
        return False

    m_right = total_m - m_left
    c_right = total_c - c_left

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def generate_successors(state):
    m_left, c_left, boat = state
    successors = []

    for m_move, c_move in moves:

        if boat == 1:
            # boat on LEFT → move to RIGHT
            new_m = m_left - m_move
            new_c = c_left - c_move
            new_boat = 0
        else:
            # boat on RIGHT → move to LEFT
            new_m = m_left + m_move
            new_c = c_left + c_move
            new_boat = 1

        if is_valid(new_m, new_c):
            successors.append((new_m, new_c, new_boat))

    return successors