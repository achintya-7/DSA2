arr = [2, 2, 3, 1, 2, 4, 2]

def better(arr) -> int:
    dict = {}

    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for key, value in dict.items():
        if value > len(arr) // 2:
            return key
        else:
            return -1


def best(arr) -> int:
    cnt = 0
    element = -1

    for num in arr:
        if cnt == 0:
            cnt = 1
            element = num

        elif num == element:
            cnt = cnt + 1

        else:
            cnt = cnt - 1 

    check = 0
    for num in arr:
        if num == element:
            check = check + 1

    if check > len(arr) // 2:
        return element
    else:
        return -1


if __name__ == '__main__':
    print(best(arr))