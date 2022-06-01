


ans_list = []

for i in range(1,10000):

    ans = 0

    for j in [3,4,5,6,7]:
        if i % j ==0:
            ans +=1
    
    if ans == 3:
        ans_list.append([i, ans])
        print(i)

    ans_list.append(ans)


print(ans_list)