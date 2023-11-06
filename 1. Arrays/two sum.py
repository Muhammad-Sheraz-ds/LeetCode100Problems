def twoSum(numbers, target):
    result = [0, 0]
    map = {}

    for i in range(len(numbers)):
        complement = target - numbers[i]

        if complement in map:
            result[1] = i
            result[0] = map[complement]
            return result

        map[numbers[i]] = i

    return result
