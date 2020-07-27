def det(mat):
    col_idx = len(mat[0])
    result = 0
    for c in range(col_idx):
        one_c = c + 1
        two_c = one_c + 1
        if one_c > 2:
            one_c -= 3
        if two_c > 2:
            two_c -= 3
        det = mat[0][c] * ((mat[1][one_c]*mat[2][two_c]) - (mat[1][two_c]*mat[2][one_c]))
        result += det
    print("이 행렬의  행렬식은 \n")
    return result
    
A = []

for i in range(3):
    row_number = list(map(int, input("행렬의 {}번째 행의 원소를 입력하세요 : \n".format(i+1)).split()))
    A.append(row_number)
    
from pprint import pprint
pprint(det(A))
