def permute(nums):
    from itertools import permutations

    k = []

    for p in permutations(nums):
        k.append(p)

    return k
