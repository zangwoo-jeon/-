def inverse(mat):
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
    inverse_mat = []
    
    try:
        det = 1 / ((mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0]))
    except ZeroDivisionError:
        a = print("det가 0이므로 존재하지 않는다")
        return a
    det = 1 / ((mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0]))
    mat[0][0], mat[1][1] = mat[1][1], mat[0][0]
    mat[1][0] *= -1
    mat[0][1] *= -1
    for c in range(col_idx):
        result = [det*mat[c][r] for r in row_idx]
        inverse_mat.append(result)
            
    return inverse_mat
    
n = int(input("행의 갯수를 입력하세요 : \n"))
A = []
B = []

for i in range(n):
    number1 = list(map(int, input("첫번째 행렬의 {}번째 행의 원소를 입력하세요 : \n".format(i+1)).split()))
    A.append(number1)

    
from pprint import pprint
print("해당 행렬의 역행렬은")
pprint(inverse(A))