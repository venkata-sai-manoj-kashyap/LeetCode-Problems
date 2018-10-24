def main():
    # first = [9, 6, 8, 3, 6, 4, 1, 8, 5, 1]
    # second = [9, 9, 9, 5, 7, 8, 8, 10, 8, 2]
    # values = [17, 29, 3, 20, 11, 8, 3, 23, 5, 15]
    # query = [6, 1, 8, 9, 6, 4, 3]
    # n = 10
    # solution(n, first, second, values, query)
    first = [8, 1, 2, 2, 5, 1, 3, 6, 6]
    second = [8, 2, 4, 5, 7, 3, 6, 8, 9]
    values = [2, 4, 8, 5, 6, 7, 7, 11, 4]
    query = [1, 2, 3, 6, 5]
    n = 9
    print(solution(n, first, second, values, query))
    # for i in range(0, 10):
    #     print(i, prime_check(i))


def prime_check(val):
    if val == 4:
        return False

    for i in range(2, val//2):
        if val % i == 0:
            return False
    return True


def solution(n, first, second, values, query):
    tree = {}
    node = {}

    for i in range(len(first)):
        if first[i] == second[i]:
            continue
        if first[i] in tree:
            tree[first[i]].add(second[i])
            if second[i] in tree:
                tree[second[i]].add(first[i])
            else:
                tree[second[i]] = {first[i]}
        else:
            tree[first[i]] = {second[i]}
            if second[i] in tree:
                tree[second[i]].add(first[i])
            else:
                tree[second[i]] = {first[i]}

    for i in range(len(values)):
        node[i+1] = values[i]

    prime_tree = recursive(tree, node, 1, set(), {})

    # for i in sorted(tree.keys()):
    #     print(i, prime_tree[i])

    for i in range(len(query)):
        if query[i] in prime_tree:
            query[i] = prime_tree[query[i]]
        else:
            query[i] = 0
    return query


def recursive(tree, node, curr, looked, prime_tree):
    if_leaf = 0
    looked.add(curr)
    for i in tree[curr]:
        if i in looked:
            if_leaf += 1

    if if_leaf == len(tree[curr]):
        if prime_check(node[curr]):
            prime_tree[curr] = 1
        else:
            prime_tree[curr] = 0

        return prime_tree
    else:
        prime_count = 0
        for i in tree[curr]:
            if i not in looked:
                prime_tree = recursive(tree, node, i, looked, prime_tree)
                prime_count += prime_tree[i]
        if prime_check(node[curr]):
            prime_count += 1

        prime_tree[curr] = prime_count

        return prime_tree


if __name__ == "__main__":
    main()
