import matplotlib.pyplot as plt
from itertools import cycle


def neighbourhood(iterable):
    iterator = cycle(iterable)
    prev_item = iterable[-1]
    current_item = next(iterator)
    for next_item in iterator:
        yield prev_item, current_item, next_item
        prev_item = current_item
        current_item = next_item


def step(state: list, rules: dict) -> list:
    neighbourhoods = neighbourhood(state)
    new_state = []
    for _ in range(len(state)):
        n = next(neighbourhoods)
        new_state.append(rules[n])
    return new_state


if __name__ == '__main__':
    r = {
        (0, 0, 0): 0,
        (0, 0, 1): 1,
        (0, 1, 0): 1,
        (0, 1, 1): 1,
        (1, 0, 0): 1,
        (1, 0, 1): 0,
        (1, 1, 0): 0,
        (1, 1, 1): 0
    }

    xs = [0] * 200 + [1] + [0] * 200

    rows = []

    for _ in range(200):
        xs = step(xs, r)
        rows.append(xs)

    plt.figure(figsize=(10, 10))
    plt.imshow(rows, cmap="Greys")
    plt.axis("off")
    plt.show()
