from collections import deque


def search(lines, pattern, history):
    previous_lines = deque(maxlen=history)
    for i in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)
