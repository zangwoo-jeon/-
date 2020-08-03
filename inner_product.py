def inner_product(vec1, vec2):
    row_idx = list(range(len(vec1)))
    result = 0
    sum_result = 0
    for r in row_idx:
        result = vec1[r] * vec2[r]
        print("{}번 째 항들의 내적값 : ".format(r+1), result)
        sum_result += result
    return sum_result
    
A = list(map(int, input("첫 번째 벡터의 원소를 입력하세요.\n").split()))
B = list(map(int, input("두 번째 벡터의 원소를 입력하세요.\n").split()))  

from pprint import pprint
print("해당 두 벡터의 내적은 \n")
pprint(inner_product(A, B))