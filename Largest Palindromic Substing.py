def palindrome(a):
    if a == a[::-1]:
        return True
    return False


dctnry = {}


def largestpalindrome(x):
    if x in dctnry:
        return dctnry[x]

    if palindrome(x):
        dctnry[x] = x
        return x

    a = largestpalindrome(x[1:])
    b = largestpalindrome(x[:-1])
    c = largestpalindrome(x[1:-1])

    if len(a) > max(len(b), len(c)):
        dctnry[x] = a
        return a
    elif len(b) > max(len(a), len(c)):
        dctnry[x] = b
        return b
    else:
        dctnry[c] = c
        return c


print(largestpalindrome('daccacacacasbbcccckcccbcca'))