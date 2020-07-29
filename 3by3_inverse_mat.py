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
    return result

    
def TBT_inverse(mat):
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
    THT_Inverse_mat = []
    Det_A = det(mat)
    print("Det(A) = ", det(mat))
    for c in range(col_idx):
        Middle_mat = []
        for r in row_idx:
            one_c = c + 1
            two_c = one_c + 1
            one_r = r + 1
            two_r = one_r + 1
            if one_r > 2:
                one_r -= 3
            if two_r > 2:
                two_r -= 3
            if one_c > 2:
                one_c -= 3
            if two_c > 2:
                two_c -= 3
            Inverse_mat = ((mat[one_r][one_c]*mat[two_r][two_c]) - (mat[one_r][two_c]*mat[two_r][one_c])) / Det_A
            Middle_mat.append(Inverse_mat)
        THT_Inverse_mat.append(Middle_mat)
    return THT_Inverse_mat
    
A = []

for i in range(3):
    number1 = list(map(int, input("행렬의 {}번째 행의 원소를 입력하세요 : \n".format(i+1)).split()))
    A.append(number1)

    
from pprint import pprint
print("해당 행렬의 역행렬은")
pprint(TBT_inverse(A))