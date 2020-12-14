def selection_sort(arr):
    min_item = arr[-1]
    min_idx = len(arr) - 1
    
    for idx, item in enumerate(arr):
        if item < min_item:
            min_idx = idx
            min_item = item
    
    return min_item, min_idx


A = [9,6,7,3,5]
res = selection_sort(A)

for i in range(len(A)):
    min_item, min_idx = selection_sort(A)
    

print(res)