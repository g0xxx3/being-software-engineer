from collections import defaultdict


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        self.added += 1
        return 0


if __name__ == '__main__':
    counter = CountMissing()
    current = {'green': 1, 'orange': 2}
    result = defaultdict(counter, current)

    increments = [('red', 20), ('green', 10), ('blue', 35)]
    for key, offset in increments:
        result[key] += offset

    print(counter.added)
