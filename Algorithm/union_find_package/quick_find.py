class QuickFind:
    def __init__(self, item_count):
        self.item_count = item_count
        self.edge = [x for x in range(self.item_count)]
        pass

    def find(self, x):
        return self.edge[x]

    def union(self, p, q):
        dp = self.find(p)
        dq = self.find(q)

        if dp == dq:
            pass

        for x in range(self.item_count):
            if self.edge[x] == dp:
                self.edge[x] = dq
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)
