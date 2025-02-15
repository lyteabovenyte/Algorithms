from itertools import tee

def sliding_window(iterable, n):
    iterators = tee(iterable, 3)

    for i, it in enumerate(iterators):
        for _ in range(i):
            next(it, None)
        
    return list(zip(*iterators))

print(sliding_window([3, -1, 2, 6, 4, 5, 8], 3))

# is we want varibale size up to a max_n
def sliding_window_variable(iterable, max_n):
    for n in range(max_n, 0, -1):
        yield from sliding_window(iterable, n)

print(list(sliding_window_variable([3, -1, 2, 6, 4, 5, 8], 3)))
