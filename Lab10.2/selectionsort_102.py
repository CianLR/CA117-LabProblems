def selectionsort(A):
    for i in range(len(A)):
        min_j = i
        for j in range(i, len(A)):
            if A[j] < A[min_j]:
                min_j = j
        A[i], A[min_j] = A[min_j], A[i]

