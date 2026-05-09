import os
import random
import numpy as np

def matrix_chain_dp(p):
    n = len(p) - 1
    m = np.zeros((n+1, n+1), dtype=int)
    s = np.zeros((n+1, n+1), dtype=int)
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = 10**9 # dùng số lớn thay cho vô cực
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return int(m[1][n]), s

def construct_parens(s, i, j):
    if i == j:
        return f"A{i}"
    else:
        return "(" + construct_parens(s, i, s[i][j]) + construct_parens(s, s[i][j] + 1, j) + ")"

def generate_testcases():
    os.makedirs('testcase', exist_ok=True)

    for tc in range(1, 21):
        N = random.randint(2, 8) 
        if tc > 15:
            N = random.randint(8, 12) # Sinh các test case lớn hơn ở cuối
            
        dims = [random.randint(2, 6) for _ in range(N + 1)]
        
        matrices = []
        for i in range(N):
            r, c = dims[i], dims[i+1]
            mat = np.random.randint(1, 10, size=(r, c)) # Random giá trị từ 1 đến 9
            matrices.append(mat)
            
        opt_cost, s_table = matrix_chain_dp(dims)
        parens = construct_parens(s_table, 1, N)
        
        # Tính kết quả nhân ma trận theo thứ tự từ trái sang phải
        # Do phép nhân ma trận có tính kết hợp nên nhân theo thứ tự nào cũng ra cùng 1 kết quả
        result = matrices[0]
        for i in range(1, N):
            result = np.dot(result, matrices[i])
            
        with open(f'testcase/input{tc}.txt', 'w') as f:
            f.write(f"{N}\n")
            for mat in matrices:
                r, c = mat.shape
                f.write(f"{r} {c}\n")
                for row in mat:
                    f.write(" ".join(map(str, row)) + "\n")
                    
        with open(f'testcase/output{tc}.txt', 'w') as f:
            f.write(f"{opt_cost}\n")
            f.write(f"{parens}\n")
            for row in result:
                f.write(" ".join(map(str, row)) + "\n")

    print("Generated 20 testcases successfully.")

if __name__ == '__main__':
    generate_testcases()
