def carParking(n, available):
    lot = [[0] * n] * n
    available = ()
    for i in range(n):
        for j in range(n):
            if lot[i][j] == 0:
                available = (i, j)
                lot[i][j] = 1
    return available


carParking(5, available)
