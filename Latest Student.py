from random import choice, randint


def solution(problem):
    name = {}
    date = {}
    attendance = {}

    # for i in problem:
    #     print(i)

    for aday in problem:
        if aday[1] not in name:
            name[aday[1]] ={}
        name[aday[1]] = {aday[0]: (int(aday[3]) - int(aday[2])), **name[aday[1]]}
        date[aday[0]] = 0

        if aday[0] in attendance:
            attendance[aday[0]] += 1
        else:
            attendance[aday[0]] = 1

    for person in name:
        for day in date:
            if day in name[person]:
                date[day] += name[person][day]

    for day in date:
        date[day] /= attendance[day]

    # for i in name:
    #     for j in name[i]:
    #         print(i, j, name[i][j])

    # for i in attendance:
    #     print(i, attendance[i])

    # for i in date:
    #     print(i, date[i])

    for aday in problem:
        name[aday[1]][aday[0]] = max(0, name[aday[1]][aday[0]] - date[aday[0]])

    # for i in name:
    #     print(i, name[i])

    dctnry = {}

    for person in name:
        for day in date:
            if day in name[person]:
                if person in dctnry:
                    dctnry[person] += name[person][day]
                else:
                    dctnry[person] = name[person][day]

    for i in sorted(dctnry.keys(), key=lambda x: dctnry[x]):
        if dctnry[i] == max(dctnry.values()):
            return i


def problem_builder():
    problem_set = []

    names = ['Raju', 'Ravi', 'Mohan', 'Seshu', 'Bhanu']
    dates = ['09-01', '09-02', '09-03', '09-04', '09-05']

    counter = 0
    for i in range(randint(3, 10)):
        start_time = randint(600, 700)

        if dates:
            date = choice(dates)
            del dates[dates.index(date)]

            for j in range(len(names)):
                if randint(0, 100) % 2 == 0:
                    problem_set.append([])
                    problem_set[counter].append(date)
                    problem_set[counter].append(names[j])
                    problem_set[counter].append(str(start_time))
                    problem_set[counter].append(str(start_time + randint(0, 100)))
                    counter += 1

    return sorted(problem_set, key=lambda x: int(x[0][3:5]))


def main():
    problem = problem_builder()
    for i in problem:
        print(i, 'Late by', int(i[3]) - int(i[2]), 'minutes')
    print('\nLatest Student:', solution(problem))


if __name__ == "__main__":
    main()
