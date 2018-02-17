"""
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an arrya A:
A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0
3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0
7 is not an equilibrium index, because it is not a valid index of array A.
Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.
"""


def find_equilibrium_index(items):
    total = sum(items)
    left_sum = 0
    indices = []
    for i, item in enumerate(items):
        total -= item
        if total == left_sum:
            indices.append(i)
        left_sum += item

    return indices


if __name__ == '__main__':
    print(find_equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))
    print(find_equilibrium_index([-2, 3, 4, 0, 2, 3]))
    print(find_equilibrium_index([12, 34, 8, 9, 45, 91, 3, 1]))