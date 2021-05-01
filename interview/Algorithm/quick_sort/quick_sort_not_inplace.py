def _sort(l, _reversed=False):

    if len(l) <= 1:
        return l

    pivot = l[0]
    left, same, right = [], [], []

    for num in l:
        if num < pivot: left.append(num)
        elif num > pivot: right.append(num)
        else: same.append(num) 

    if _reversed:
        return _sort(right, _reversed=True) + same + _sort(left, _reversed=True)

    return _sort(left) + same + _sort(right)

if __name__=="__main__":
    init_list = [5,3,1,4,2,6,4,1]
    
    a_sorted_list = _sort(init_list)
    d_sorted_list = _sort(init_list, _reversed=True)
    
    print(*a_sorted_list)
    print(*d_sorted_list)