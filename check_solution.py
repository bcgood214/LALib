from gauss_elimination import *
import matrix_matrix_multiplication as mm

def check_solution(mat, b):
    a1 = mat[:-1]
    a2 = mat[-1]
    b_sub = b[:-1]
    a1 = gauss_elimination(a1)
    res = forward_sub(a1, b_sub)
    res = find_vals(a1, res)
    print(a2)
    print(res)
    solution = mm.row_col_multiplication(a2, res)
    print(solution)
    return solution == b[-1]

if __name__ == "__main__":
    m = [
        [1, -2, 4],
        [1, 0, 0],
        [1, 2, 4],
        [1, 4, 16]
    ]
    res = [-1, 2, 3, 9]
    print(check_solution(m, res))