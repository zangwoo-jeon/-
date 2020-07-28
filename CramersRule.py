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

def Cramer(mat1, mat2):
    row_idx = list(range(len(mat1)))
    col_idx = len(mat1[0])
    result = 0
    change_mat = mat1
    Det_A = det(mat1)
    print("det(A) = ", det(mat1))
    for c in range(col_idx):
        temp = []
        for r in row_idx:
            temp.append(change_mat[r][c])
            change_mat[r][c] = mat2[r]
        print("Change_Mat", change_mat)
        Det_x = det(change_mat)
        print("det(X{}) = ".format(c+1), Det_x)
        result = Det_x / Det_A
        print("X{} = ".format(c+1), result)
        for r in row_idx:
            change_mat[r][c] = temp[r]
        

A = []
B = []

for i in range(3):
    row_number = list(map(int, input("계수행렬의 {}번째 행의 원소를 입력하세요 : \n".format(i+1)).split()))
    A.append(row_number)
    
for j in range(3):
    B_number = int(input("상수행렬의 {}번째 행의 원소를 입력하세요. \n".format(j+1)))
    B.append(B_number)

Cramer(A, B) 
 
#from pprint import pprint
#pprint(Cramer(A, B))