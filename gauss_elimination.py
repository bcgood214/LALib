from decimal import DivisionByZero
from random import gauss
from turtle import forward

def gauss_elimination(mat):
    row_ind = 0
    for i in range(len(mat)-1):
        for j in range(i+1, len(mat)):
            try:
                mat[j][row_ind] = mat[j][row_ind]/mat[i][row_ind]
            except ZeroDivisionError:
                return (False, i, row_ind)
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

def solve_for_x(a, vals, res):
    if len(vals) > 0:
        print(vals)
        for i in range(len(vals)):
            a_ind = -1*(i+1)
            a[a_ind] *= vals[a_ind]
            res += -1*a[a_ind]
    res /= a[0]
    return res
    

def find_vals(mat, res):
    vals = []
    for i in range(1, len(mat)+1):
        vals.insert(0, solve_for_x(mat[-i][-i:], vals, res[-i]))
    return vals

def slice(mat, v):
    lv = len(v)
    return mat[:lv], mat[lv:]

if __name__ == "__main__":
    m = [
        [2, 0, 1, 2],
        [-2, -1, 1, -1],
        [4, -1, 5, 4],
        [-4, 1, -3, -8]
    ]
    m2 = [
        [1, -2, 4],
        [1, 0, 0],
        [1, 2, 4]
    ]

    m2 = gauss_elimination(m2)
    res = forward_sub(m2, [-1, 2, 3])
    print(m2)
    print(res)
    print(find_vals(m2, res))
