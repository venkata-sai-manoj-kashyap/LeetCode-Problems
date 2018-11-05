def isvalid_parathesis(x):
    stack = []
    dctnry = {')': '('}
    for val in x:
        if val in dctnry and not stack:
            return False
        elif val == '(':
            stack.append(val)
        elif val == ')':
            stack.pop()
        else:
            return False

    if not stack:
        return True


def recursive(x, x_length, open_braces, close_braces, max_length, ret):
    if x_length == max_length:
        ret.add(x)
        return ret

    if open_braces == close_braces:
        ret = recursive(x + "(", x_length+1, open_braces+1, close_braces, max_length, ret)
        return ret

    if open_braces >= max_length/2:
        ret = recursive(x+")", x_length+1, open_braces, close_braces+1, max_length, ret)
        return ret

    ret = recursive(x + "(", x_length+1, open_braces+1, close_braces, max_length, ret)
    ret = recursive(x + ")", x_length+1, open_braces, close_braces+1, max_length, ret)

    return ret


def main():
    n = 10
    result = recursive("(", 1, 1, 0, 2*n, set())
    print(result)


if __name__ == '__main__':
    main()