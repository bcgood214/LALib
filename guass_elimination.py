def gauss_elimination(mat):
    row_ind = 0
    for i in range(len(mat)-1):
        for j in range(i+1, len(mat)):
            if mat[i][row_ind] == 0:
                if i+1 <= len(mat)-1:
                    temp = mat[i]
                    mat[i] = mat[i+1]
                    mat[i+1] = temp
            mat[j][row_ind] = mat[j][row_ind]/mat[i][row_ind]
            for k in range(row_ind+1, len(mat[0])):
                mat[j][k] = mat[j][k] - (mat[j][row_ind]*mat[i][k])
        row_ind += 1
    return mat

def forward_sub(mat, res):
    row_ind = 0
    for i in range(len(mat)-1):
        for j in range(i+1, len(mat)):
            res[j] = res[j] - mat[j][row_ind]*res[i]
        row_ind += 1
    
    return res

def back_sub(mat, res):
    pass

if __name__ == "__main__":
    m = [
        [2, 0, 1, 2],
        [-2, -1, 1, -1],
        [4, -1, 5, 4],
        [-4, 1, -3, -8]
    ]
    m2 = [
        [2, 4, -2],
        [4, 8, 6],
        [6, -4, 2]
    ]

    m2 = gauss_elimination(m2)
    print(m2)
    res = [-10, 20, 18]
    print(forward_sub(m2, res))