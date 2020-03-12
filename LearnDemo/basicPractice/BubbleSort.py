"""
bubble sort
"""
bu_list = [1,3,2,6,0,9,54,4,32,8]

re_list = range(len(bu_list))[::-1]

for i in re_list:
    for j in range(i):
        if bu_list[j] > bu_list[j+1]:
            bu_list[j],bu_list[j+1] = bu_list[j+1],bu_list[j]

print(bu_list) 