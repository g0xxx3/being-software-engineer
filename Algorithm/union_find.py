# 10
# 4 3
# 3 8
# 6 5
# 9 4
# 2 1
# 8 9
# 5 0
# 7 2
# 6 1
# 1 0
# 6 7


from union_find_package.quick_find import QuickFind
from union_find_package.quick_union import QuickUnion
from union_find_package.weighted_quick_union import WeightedQuickUnion
quick_find = QuickFind(10)
quick_union = QuickUnion(10)
weighted_quick_union = WeightedQuickUnion(10)


quick_find.union(0, 4)
quick_find.union(1, 0)
quick_find.union(2, 0)
quick_find.union(1, 5)

quick_union.union(0, 4)
quick_union.union(1, 0)
quick_union.union(2, 0)
quick_union.union(2, 5)
quick_union.union(0, 5)
quick_union.union(0, 3)

weighted_quick_union.union(0, 4)
weighted_quick_union.union(1, 0)
weighted_quick_union.union(2, 0)
weighted_quick_union.union(2, 5)
weighted_quick_union.union(0, 5)
weighted_quick_union.union(0, 3)

print(quick_find.connected(1, 5))
print(quick_union.connected(1, 5))
print(weighted_quick_union.connected(2, 5))
