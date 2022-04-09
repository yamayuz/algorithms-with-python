# 改善前
def dot_product(x, y):
    matrix_out = []

    for i in range(len(x)):
        matrix_temp = [0] * len(y[0])

        for j in range(len(y)):
            for k in range(len(y[0])):
                matrix_temp[k] += x[i][j] * y[j][k]

        matrix_out.append(matrix_temp)

    return matrix_out


# 改善後
def dot_product_imp(x, y):
    matrix_out = [[0 for j in range(len(x))] for i in range(len(y[0]))]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                matrix_out[i][j] += x[i][k] * y[k][j]

    return matrix_out