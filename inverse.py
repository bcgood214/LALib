from functools import reduce


def order_by_leading(m):
    leading = len(m)
    leading_pos = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                leading_pos.append((i, j))
                break
        # for k in range(i+1, len(m)):
        #     for j in range(len(m[k])):
        #         if m[j] != 

    new_mat = []
    for i in range(len(leading_pos)):
        for j in range(i+1, len(leading_pos)):
            if leading_pos[j][1] < leading_pos[i][1]:
                leading_pos[j], leading_pos[i] = leading_pos[i], leading_pos[j]
    
    for elem in leading_pos:
        ind = elem[0]
        new_mat.append(m[ind])
    
    return new_mat

def row_reduction(m, r1, r2, elem_ind):
    scalar = m[r2][elem_ind]/m[r1][elem_ind]
    m[r2] = [m[r2][i] - scalar*m[r1][i] for i in range(len(m[r2]))]

    return m

def echelon_form(m):
    m = order_by_leading(m)

    for i in range(len(m)):
        leading = None
        for elem in range(len(m[i])):
            # print(f"{m}, {i}")
            if m[i][elem] != 0:
                leading = elem
                break
        
        for j in range(i+1, len(m)):
            if leading is not None and m[j][leading] != 0:
                m = row_reduction(m, i, j, leading)
        
    return m

def reduce_leading(m):
    for i in range(len(m)):
        for elem in range(len(m[i])):
            if m[i][elem] != 0:
                m[i] = [m[i][j]/m[i][elem] for j in range(len(m[i]))]
                break
    
    return m

def rref(m):
    m = reduce_leading(m)
    for i in range(1, len(m)):
        leading = None
        for elem in range(len(m[i])):
            if m[i][elem] != 0:
                leading = elem
                break

        for j in range(i):
            if leading is not None and m[j][leading] != 0:
                m = row_reduction(m, i, j, leading)
    
    return m

def append_identity(m):
    row_num = len(m)
    col_num = len(m[0])
    id_mat = []
    for i in range(row_num):
        id_mat.append([0 for c in range(col_num)])
        if i < col_num:
            id_mat[i][i] = 1
        m[i] = m[i] + id_mat[i]
    
    return m

def get_lu(mat):
    l = [[0 for j in range(len(mat))] for i in range(len(mat))]
    for i in range(len(l)):
        l[i][i] = 1

    l_col = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                for k in range(i+1, len(mat)):
                    if mat[k][j] != 0:
                        scalar = mat[k][j]/mat[i][j]
                        for m in range(j, len(mat[k])):
                            mat[k][m] = mat[k][m] - (mat[i][m] * scalar)
                        l[k][l_col] = scalar
                l_col += 1
                break
    
    return l, mat

def find_inverse(m):
    m = append_identity(m)
    m = order_by_leading(m)
    m = echelon_form(m)
    m = rref(m)
    return m

if __name__ == "__main__":
    m = [
        [0, 1, 2],
        [1, 0, 3],
        [0, 0, 1]
    ]
    m2 = [
        [0.5, 0, 1],
        [0, 1, 0],
        [0, 0, 1]
    ]
    m3 = [
        [1, 0, -2],
        [3, 1, -2],
        [0, -1, -1]
    ]
    a = [
        [4, -3, -1, 5],
        [-16, 12, 2, -17],
        [8, -6, -12, 22]
    ]

    print(get_lu(a))

    # m = append_identity(m2)
    # print(m)
    # m = order_by_leading(m)
    # print(m)
    # m = echelon_form(m)
    # print(m)
    # m = rref(m)
    # print(m)