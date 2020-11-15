# def findNumberOfLIS(num):
#     if len(nums) == 0:
#         return 0
#     length = [1] * len(nums)
#     count = [1] * len(nums)
#     length[0], count[0] = 1, 1
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[j] < nums[i]:
#                 if length[j] + 1 == length[i]:
#                     count[i] += count[j]
#                 elif length[j] + 1 > length[i]:
#                     length[i] = length[j] + 1
#                     count[i] = count[j]

#     max_len = max(length)
#     return sum([count[i] for i in range(len(count)) if length[i] == max_len])

# print(findNumberOfLIS([1, 4, 2, 6, 5, 3]))

# def lis(a):
# 	L = []
# 	for (k,v) in enumerate(a):
# 		L.append(max([L[i] for (i,n) in enumerate(a[:k]) if n<v] or [[]], key=len) + [v])
# 	return max(L, key=len)

# inp = [int(a) for a in input("List of integers: ").split(' ')]
# print(lis(inp));

st = [] 

def find(inp, out) : 
    if len(inp)== 0 : 
        if len(out) != 0 : 
            st.append(out) 
        return
  
    find(inp[1:], out[:]) 

    if len(out)== 0: 
        find(inp[1:], inp[:1]) 
    elif inp[0] > out[-1] : 
        out.append(inp[0]) 
        find(inp[1:], out[:]) 
  
# The input list 
ls1 = [1, 4, 2, 6, 5, 3] 
ls2 = [] 
  
# Calling the function 
find(ls1, ls2) 
print(st)