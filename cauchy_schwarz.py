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
   
def inner_product(mat1, mat2):
    row_idx = list(range(len(mat1)))
    result = 0
    sum_result = 0
    for r in row_idx:
        result = mat1[r] * mat2[r]
        print("{}번 째 항들의 내적값 : ".format(r+1), result)
        sum_result += result
    return sum_result

def Cauchy(mat1, mat2):
    Norm1 = norm(mat1)
    print("|x| = ", Norm1)
    Norm2 = norm(mat2)
    print("|y| = ", Norm2)
    print("|x| * |y| = ", Norm1*Norm2)
    Inner = inner_product(mat1, mat2)
    print("|x·y| = ", Inner)
    if Inner <= Norm1*Norm2:
        print("코시 슈바르츠가 성립한다.\n")
    else:
        print("코시 슈바르츠가 성립하지 않는다.\n")
    
A = list(map(int, input("첫 번째 벡터의 원소를 입력하세요.\n").split()))
B = list(map(int, input("두 번째 벡터의 원소를 입력하세요.\n").split()))  

   

    
from pprint import pprint
print("이 벡터는 \n")
pprint(Cauchy(A, B))