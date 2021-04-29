'''
시작 21:37
제출 
종료 
''' 

def get_end_idx(start_idx):
    stack = []
    for i in range(start_idx, len(l)):
        if l[i] == '(': stack.append(l[i])
        elif l[i] == ')': stack.pop()
        if len(stack) == 0: return i

def solve(start_idx, end_idx):
    rec_answer = 0
    idx = start_idx

    while True:

        if idx >= end_idx:
            break
        
        if idx == len(l)-1:
            if l[idx].isdigit():
                rec_answer += 1
                idx += 1
                continue
        
        if l[idx+1].isdigit() or (l[idx].isdigit() and l[idx+1] == ')'):
            rec_answer += 1 
            idx += 1
            continue
        
        if l[idx+1] == '(':
            _end_idx = get_end_idx(idx+1)
            rec_answer += int(l[idx]) * solve(idx+2, _end_idx)
            idx = _end_idx+1
            continue
    
    return rec_answer
        
answer = 0
l = list(input())
if '(' in l: print(solve(0,len(l)))
else: print(len(l))