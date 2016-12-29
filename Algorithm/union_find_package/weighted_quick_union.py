class WeightedQuickUnion:
    def __init__(self, item_count):
        self.item_count = item_count
        self.edge = [x for x in range(self.item_count)]
        self.weight = [1]*item_count
        pass

    def find(self, x):
        while x != self.edge[x]:
            x = self.edge[x]

        return x

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            pass

        if self.weight[p_root] < self.weight[q_root]:
            self.edge[p_root] = q_root
            self.weight[p_root] += self.weight[q_root]
        else:
            self.edge[q_root] = p_root
            self.weight[q_root] += self.weight[p_root]

        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)
