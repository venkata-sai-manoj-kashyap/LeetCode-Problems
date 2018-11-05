def main():
    letter_combination("23")


def recursive(num, dctnry, ind, result, word):
    if ind >= len(num):
        result.append(word)
        return result

    for i in dctnry[num[ind]]:
        result = recursive(num, dctnry, ind+1, result, word+i)

    return result


def letter_combination(num):
    dctnry = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    print(recursive('23', dctnry, 0, [], ''))


if __name__ == "__main__":
    main()