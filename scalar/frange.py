def frange(start, end, step=1):
    x = start
    while x < end:
        yield x
        x += step
