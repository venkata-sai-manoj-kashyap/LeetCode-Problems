from itertools import permutations
from copy import deepcopy


def combinationSum(candidates, target):
    result = []
    combinationSumRecu(sorted(candidates), result, 0, [], target)
    return result


def combinationSumRecu(candidates, result, start, intermediate, target):
    if target == 0:
        result.append(list(intermediate))
    while start < len(candidates) and candidates[start] <= target:
        intermediate.append(candidates[start])
        combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
        intermediate.pop()
        start += 1


def findSchedules(work_hour, day_hours, pattern):
    pattern = list(pattern)
    total_available = 0
    question_count = 0

    for i in pattern:
        if i != '?':
            total_available += int(i)
        else:
            question_count += 1

    total_available = work_hour - total_available

    if total_available <= 0:
        for i in range(len(pattern)):
            if pattern[i] != '?':
                if pattern[i] > work_hour:
                    pattern[i] = work_hour

        for i in pattern:
            if i != '?':
                total_available += int(i)
            else:
                question_count += 1

        total_available = work_hour - total_available

        if total_available >= 0:
            return ''.join(pattern).replace('?', '0')

    new_list = []
    for i in range(1, day_hours+1):
        new_list.append(i)

    return_list = combinationSum(new_list, total_available)

    i = 0
    while i < len(return_list):
        if len(return_list[i]) > question_count:
            del return_list[i]
            continue
        elif len(return_list[i]) < question_count:
            return_list[i] += [0]*(question_count - len(return_list[i]))

        i += 1

    final_set = set()

    for i in return_list:
        for j in permutations(i, len(i)):
            final_set.add(j)

    return_list = []
    old_pattern = deepcopy(pattern)

    for schedule in sorted(final_set):
        counter = 0
        pattern = deepcopy(old_pattern)
        for i in range(len(pattern)):
            if pattern[i] == '?':
                pattern[i] = str(schedule[counter])
                counter += 1

        return_list.append(''.join(pattern))
    return return_list


print(findSchedules(20, 8, '??888??'))
