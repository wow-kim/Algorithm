def solution(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range (len(result)):
        for j in range (len(result[0])):
            for k in range (len(arr1[0])):
                result[i][j] += arr1[i][k]*arr2[k][j]

    return result

#------------------------------------------------------------------------
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]