# Added after mult
def row_col_multiplication(x1, x2):
    val = 0
    for i in range(len(x1)):
        val += x1[i]*x2[i]
    
    return val

def mult(a, b):
    if len(a[0]) != len(b):
        return False
    
    c = [ [0]*(len(b[0])) for i in range(len(a))]
    print(len(c))
    print(len(c[0]))

    for i in range(len(b[0])):
        for j in range(len(a)):
            v = 0
            for k in range(len(a[0])):
                v += a[j][k] * b[k][i]
            c[j][i] = v

    return c

if __name__ == "__main__":
    a = [[2, -1, 1, -1], [0, 1, 3, 1], [1, 0, 1, 1]]
    b = [[2, 0, 1], [1, 1, 0], [2, 0, 1], [1, 1, 0]]
    print(mult(b, a))