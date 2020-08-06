def cross_product(mat1, mat2):
    
    cross_mat = [["i", "j", "k"]]
    cross_mat.append(mat1)
    cross_mat.append(mat2)
    print("Cross_mat", cross_mat)
    row_idx = list(range(len(cross_mat)))
    col_idx = len(cross_mat[0])
    result_mat = []
    for r in row_idx:
        result = 0
        Middle_mat = [["i", "j", "k"]]
        one_r = r + 1
        two_r = one_r + 1
        if one_r > 2:
            one_r -= 3
        if two_r > 2:
            two_r -= 3

        Cross = ((cross_mat[1][one_r]*cross_mat[2][two_r]) - (cross_mat[1][two_r]*cross_mat[2][one_r]))  
        Middle_mat.append(Cross)
        print("Middle_mat", Middle_mat)
        result = Middle_mat[1]
        result_mat.append(result)
    return result_mat
    
A = list(map(int, input("첫 번째 벡터의 원소를 입력하세요.\n").split()))
B = list(map(int, input("두 번째 벡터의 원소를 입력하세요.\n").split()))  

from pprint import pprint
print("이 벡터들의 외적은 \n")
pprint(cross_product(A, B))