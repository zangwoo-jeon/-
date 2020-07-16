def add(mat1, mat2):
    row_idx = list(range(len(mat1)))
    row = len(mat1)
    col_idx = len(mat1[0])
    res_mat = []
    mid_mat = []
    try:
        if (row != col_idx):
                raise ValueError("")
    except ValueError:
        a = print("잠깐! 해당 행렬은 정방행렬이 아닙니다.")
        return a
    for r in row_idx:
        result = [mat1[r][c]+mat2[r][c] for c in range(col_idx)]
        mid_mat.append(result)
        res_mat.append(mid_mat[r])
    return res_mat

def transpose(mat):
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
    trans_mat = []
    for c in range(col_idx):
        result = [mat[r][c] for r in row_idx]
        trans_mat.append(result)
    return trans_mat
    


n = int(input("행의 갯수를 입력하세요 : \n"))
A = []
B = []

for i in range(n):
    number1 = list(map(int, input("첫번째 행렬의 {}번째 행의 원소를 입력하세요 : \n".format(i+1)).split()))
    A.append(number1)
    
from pprint import pprint
print("해당 행렬과 전치 행렬의 덧셈값은\n")
pprint(add(A, transpose(A)))
