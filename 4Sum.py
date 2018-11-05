from copy import deepcopy


def check(x, n_dctnry):
    dctnry = deepcopy(n_dctnry)
    if x[0] in dctnry:
        dctnry[x[0]] -= 1
    else:
        return False

    if x[1] in dctnry:
        if dctnry[x[1]]:
            dctnry[x[1]] -= 1
        else:
            return False
    else:
        return False

    if x[2] in dctnry:
        if dctnry[x[2]]:
            dctnry[x[2]] -= 1
        else:
            return False
    else:
        return False

    if x[3] in dctnry:
        if dctnry[x[3]]:
            dctnry[x[3]] -= 1
            return True
        else:
            return False
    else:
        return False


def foursum(nums, target):

    dctnry = {}
    result_list = []
    dctnry_pairs = {}

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            summ = nums[i] + nums[j]

            if summ in dctnry_pairs:
                dctnry_pairs[summ].append((nums[i], nums[j]))
            else:
                dctnry_pairs[summ] = [(nums[i], nums[j])]
            if target - summ in dctnry_pairs:
                for pair in dctnry_pairs[target-summ]:
                    result_list.append([pair[0], pair[1], nums[i], nums[j]])

    for i in nums:
        if i in dctnry:
            dctnry[i] += 1
        else:
            dctnry[i] = 1

    result = []
    for i in range(len(result_list)):
        if check(result_list[i], dctnry):
            result.append(result_list[i])

    set_list = []
    result_list = []

    for i in range(len(result)):
        k = set(result[i])

        if k not in set_list:
            set_list.append(k)
            result_list.append(result[i])

    return result_list


if __name__ == "__main__":
    for _ in foursum([0, -1, 1, -2, 2], 0):
        print(_)
