def _sort(A, first, last):

    if last < first:
        return

    pivot = A[first]
    left, right = first + 1, last

    while left <= right:
        
        while left <= last and A[left] < pivot:
            left += 1
        
        while right > first and A[right] > pivot:
            right -= 1

        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1

    A[first], A[right] = A[right], A[first]
    _sort(A, first, right - 1)
    _sort(A, right + 1, last)

if __name__=="__main__":
    Ab = [4, 2, 5, 8, 6, 2, 3, 7, 10]
    _sort(Ab, 0, len(Ab) - 1)
    print(*Ab)