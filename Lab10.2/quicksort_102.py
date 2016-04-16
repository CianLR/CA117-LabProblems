def quicksort(A, start, end):
    if end - start < 1:
        return
    
    i = j = start
    while i <= end:
        if A[i] <= A[end]:
            A[i], A[j] = A[j], A[i]
            j += 1
        i += 1
    
    quicksort(A, start, j - 2)
    quicksort(A, j, end)

