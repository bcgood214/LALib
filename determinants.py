def get_submat(mat, row, col):
    submat = []
    for i in range(len(mat)):
        if i == row:
            continue
        new_row = []
        for j in range(len(mat[0])):
            if j == col:
                continue
            new_row.append(mat[i][j])
        submat.append(new_row)
    
    return submat


def det(mat):
    if len(mat) == 2:
        if len (mat[0]) == 2 and len(mat[1]) == 2:
            return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])
        return False
    else:
        val = 0
        sign = 1
        for i in range(len(mat[0])):
            submat = get_submat(mat, 0, i)
            val += sign*mat[0][i]*det(submat)
            sign *= -1
        return val

def mult(mat, scalar):
    new_mat = []
    for i in range(len(mat)):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[i][j] * scalar)
        new_mat.append(new_row)
    
    return new_mat

if __name__ == "__main__":
    m = [
        [1, 2, 3, 4],
        [1, 0, 2, 0],
        [0, 1, 2, 3],
        [2, 3, 0, 0]
    ]

    m2 = [
        [4, -2],
        [-3, 1]
    ]