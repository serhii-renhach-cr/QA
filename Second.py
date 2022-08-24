def get_two_max():
    import random

    random_list = [random.randint(-1000, 1000) for i in range(1000)]

    print(random_list)
    asc_list = sorted(random_list)
    print(asc_list)

    result = []
    result.append(max(asc_list))
    while result[0] == asc_list[-1]:
        asc_list.pop()
    else:
        result.append(asc_list[-1])

    print(result)


get_two_max()
