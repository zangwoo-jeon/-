def vector(mat1, mat2):
    row_idx = list(range(len(mat1)))
    result_mat = []
    result = 0
    for r in row_idx:
        result = mat2[r] - mat1[r]
        result_mat.append(result)
    return result_mat
    
First_mat = []
Second_mat = []

First_mat = list(map(int, input("시작점의 원소를 입력하시오.\n").split()))
Second_mat = list(map(int, input("끝점의 원소를 입력하시오.\n").split()))

from pprint import pprint
print("해당 vector는 \n")
pprint(vector(First_mat, Second_mat))