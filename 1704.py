lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = len(lst)

sorted_lst = sorted(lst)

for i in range(n):
    lst = sorted(lst)
    print(lst)
    
    if lst == sorted_lst:
        break
