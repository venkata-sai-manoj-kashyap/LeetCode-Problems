from itertools import permutations


def permuteUnique(nums):
    li = []
    dct = {}
    for i in permutations(nums):
        if i not in dct:
            li.append(list[i])
            dct[i] = 1
 
