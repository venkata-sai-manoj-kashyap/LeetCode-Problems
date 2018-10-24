def convert(matrix):
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


def helper(zombies):
    connection = []
    for i in range(len(zombies)):
        for j in range(len(zombies)):
            if zombies[i][j] == 1:
                if not connection:
                    connection.append(set())
                    connection[0].add(i)
                    connection[0].add(j)
                else:
                    flag = 0
                    for network in connection:
                        if i in network or j in network:
                            network.add(i)
                            network.add(j)
                            flag = 1
                    if flag == 0:
                        connection.append(set())
                        connection[-1].add(i)
                        connection[-1].add(j)

    for i in range(len(zombies)):
        flag = 0
        for j in connection:
            if i in j:
                flag = 1
        if flag == 0:
            connection.append(set())
            connection[-1].add(i)

    return len(connection)


def zombiecluster(zombies):
    zombies = convert(zombies)

    for i in zombies:
        for j in i:
            print(j, end='  ')
        print()

    for i in range(len(zombies)):
        zombies[i][i] = 0
    print('\n'*3)
    return helper(zombies)


print(zombiecluster(["1100001", "1110001", "0110001", "0001100", "0001100", "0000010", "0010001"]))
