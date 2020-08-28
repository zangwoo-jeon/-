def pivoting(mat):
    row_idx = list(range(len(mat))) 
    col_idx = len(mat[0]) 
    pivot_mat = []
    for c in range(col_idx):
        rows_with_one = [k for k in row_idx if mat[k][c] == 1]
        if rows_with_one:
            for idx in rows_with_one:
                pivot_mat.append(mat[idx])
                row_idx.remove(idx)
                break
        rows_with_nonzero = [r for r in row_idx if mat[r][c] != 0]
        if rows_with_nonzero:
            for idx in rows_with_nonzero:
                pivot_mat.append(mat[idx])
                row_idx.remove(idx)
    return pivot_mat
    
def row_reduce(mat):
    rref = [] #출력할 결과값행렬 초기화
    row_idx = list(range(len(mat))) #가로(행)의 갯수
    col_idx = len(mat[0]) #세로(열)의 갯수
    for c in range(col_idx):
        rows_with_nonzero = [r for r in row_idx if mat[r][c] != 0] #각 열에서 처음으로 0이 아닌 행을 찾는다
        if rows_with_nonzero: #그것을 찾으면
            pivot = rows_with_nonzero[0] #pivot에 그 0이 아닌 첫번째 수를 넣고    
            if len(rows_with_nonzero) == 1: #만약 그 열에서 0이 아닌 행렬이 유일하고
                if mat[pivot][c] != 0 and mat[pivot][c] != 1: #그 행, 열이 0 혹은 1이 아니면
                    mat[pivot] = [a/mat[pivot][c] for a in mat[pivot]] #그 값으로 그 행의 값들을 나눠줘서 첫 행의 값을 1로 만든다.
            for r in rows_with_nonzero: 
                if r is not pivot: #똑같은 열에서 0이 아닌 행이 2개 이상 발견되면
                    multiplier = mat[r][c] / mat[pivot][c] #그 열에서 각 행의 값들을 나눠준뒤
                    mat[r] = [a - multiplier*b for a, b in zip(mat[r], mat[pivot])] #그 값을 빼서 0으로 만든다(행사다리꼴로 만들어준다.)  
                    mat[pivot] = [a/mat[pivot][c] for a in mat[pivot]]
            row_idx.remove(pivot) #row_idx에서 그 수를 뺴고
            rref.append(mat[pivot]) #rref에 그 행의 값을 넣는다. 이걸 row_idx가 다 사라질떄까지 반복
    for r in row_idx:
        rref.append(mat[r]) #행사다리꼴로 만들어준 값을 rref에 추가
    return rref

def reduced_row(mat):
    Mat = row_reduce(pivoting(mat)) # Mat = rref
    print("Mat", Mat)
    reduced_mat = []
    Erow_idx = len(Mat)
    row_idx = list(range((len(Mat)))) #가로(행)의 갯수
    col_idx = len(Mat[0]) #세로(열)의 갯수
    rrow_idx = list(range((len(Mat)-1)))
    for c in range(col_idx-1):
        if Mat[-1][-1] == 0 and Mat[-1][-2] == 0:
            rows_with_nonzero = [r for r in rrow_idx if Mat[-2-r][-1-c] != 0]
            print("c", c)
            print("nonzero", rows_with_nonzero)
            if rows_with_nonzero:
                pivot = rows_with_nonzero[0]
                for r in rows_with_nonzero:
                    if r is not pivot:
                        multiplier = Mat[pivot][c+1] / Mat[r][c+1]
                        print("multi", multiplier)
                        Mat[pivot] = [a - multiplier*b for a, b in zip(Mat[pivot], Mat[r])]
                rrow_idx.remove(pivot)
                row_idx.remove(pivot)
                reduced_mat.append(Mat[pivot])
        else:
            rows_with_nonzero = [r for r in row_idx if Mat[r][-2-c] != 0]
            print("c", c)
            print("nonzero", rows_with_nonzero)
            if rows_with_nonzero:
                pivot = rows_with_nonzero[-1]
                for r in rows_with_nonzero:
                    if r is not pivot:
                        print("Mat[pivot]", Mat[pivot])
                        multiplier = Mat[r][-2-c] / Mat[pivot][-2-c]
                        print("multi", multiplier)
                        Mat[r] = [a - multiplier*b for a, b in zip(Mat[r], Mat[pivot])]
                        print("Mat[r]", Mat[r])
                reduced_mat.append(Mat[pivot])
                print("RI", row_idx)
                row_idx.remove(pivot)
                        
    for r in row_idx:
        reduced_mat.append(Mat[r])
    reduced_mat.reverse()
    return reduced_mat
    
n = int(input("행의 갯수를 입력하세요\n"))
A = []

for i in range(n):
    number = list(map(int, input("행렬의 {}번째 행의 원소를 입력하세요.\n".format(i+1)).split()))
    A.append(number)

    
from pprint import pprint
print("해당 행렬의 행사다리꼴은\n")
pprint(reduced_row(A))
