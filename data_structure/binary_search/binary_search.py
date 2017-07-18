def binary_search(data, target):
    """
    데이터가 정렬된 상태로 전달 되어야 합니다.
    """
    # data.sort()
    start = 0
    end = len(data) -1

    while start <= end:
        midpoint = (start + end) // 2
        if data[midpoint] == target:
            return midpoint
        elif target < data[midpoint]:
            end = midpoint -1
        else:
            start = midpoint + 1

    return None

if __name__ == "__main__":
    li = [i for i in range(11)]
    target = 5

    idx = binary_search(li, target)

    if idx:
        print(li[idx])
    else:
        print("There is no such data")

    print(help(binary_search))