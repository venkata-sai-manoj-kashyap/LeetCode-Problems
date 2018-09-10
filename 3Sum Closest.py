def threeSumClosest(nums, target):
    nums.sort()
    minn = 9999
    lengt = len(nums)
    for i in range(lengt):
        j = i + 1
        k = lengt - 1
        while j < k:
            summ = nums[i] + nums[j] + nums[k]
            diff = abs(target - summ)
            if diff == 0:
                return summ
            if diff < minn:
                minn = diff
                result = summ

            if summ < target:
                j += 1
            else:
                k -= 1

    return result