def mul(mat1, mat2):
    row_idx1 = list(range(len(mat1)))
    row_idx2 = list(range(len(mat2)))
    col_idx1 = len(mat1[0])
    col_idx2 = len(mat2[0])
    res_mat = []        
    for r in row_idx1:
        mid_mat = []
        for c2 in range(col_idx2):
            each_element = 0
            for c1 in range(col_idx1):
                each_element += mat1[r][c1]*mat2[c1][c2]
            mid_mat.append(each_element)  
        res_mat.append(mid_mat) 
    return res_mat
    
def transpose(mat):
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
    trans_mat = []
    for c in range(col_idx):
        result = [mat[r][c] for r in row_idx]
        trans_mat.append(result)
    print("이 행렬의 전치 행렬은 \n")
    return trans_mat
    
n = int(input("행의 갯수를 입력하세요 : \n"))
A = []
B = []

for i in range(n):
    number1 = list(map(int, input("첫번째 행렬의 {}번째 행의 원소를 입력하세요 : \n".format(i+1)).split()))
    A.append(number1)

    
from pprint import pprint
pprint(mul(A, transpose(A)))
