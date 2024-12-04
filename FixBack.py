def dis_calc (a, b, c):

    di = ((b**2) - (4 * a * c))**5

    if di > 0
        x = (- b + di) / (2 * a)
        y = (- b - di) / (2 * a)
        return x, y
    if di == 0:
        x = b / 2 * a
        return x
    else:
        return 0
