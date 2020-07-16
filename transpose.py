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
pprint(transpose(A))
