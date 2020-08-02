import math

def norm(mat):
    row_idx = list(range(len(mat)))
    result = 0
    middle_result = 0
    norm_result = 0
    for r in row_idx:
        result = mat[r]**2
        middle_result += result
    norm_result = math.sqrt(middle_result)
    return norm_result
    
def unit_vector(mat):
    row_idx = list(range(len(mat)))
    Norm = norm(mat)
    result = 0
    unit = []
    for r in row_idx:
        result = mat[r] / Norm
        unit.append(result)
    return unit

A = []
A = list(map(int, input("벡터의 값을 입력하시오.\n").split()))
    
from pprint import pprint
print("이 벡터의 노름과 단위 벡터(unit vector)는 \n")
pprint(norm(A))
pprint(unit_vector(A))