# O(n**2)のオーダーで計算
def maximum_profit_n2(input: list) -> int:
    output = input[1] - input[0]

    for j in range(1, len(input)):
        for i in range(0, j):
            diff = input[j] - input[i]
            if output < diff: output = diff

    return output


# O(n)のオーダーで計算
def maximum_profit_n(input: list) -> int:
    maxv = input[1] - input[0]
    minv = input[0]

    for i in range(1, len(input)):
        maxv = max(maxv, input[i] - minv)
        minv = min(minv, input[i])

    return maxv