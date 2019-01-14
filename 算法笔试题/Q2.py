dao = [[4, 4, 4, 4, 4, 4, 4, 4],
       [4, 1, 1, 1, 1, 1, 1, 4],
       [4, 1, 1, 0, 0, 0, 1, 4],
       [4, 1, 0, 0, 0, 1, 0, 4],
       [4, 1, 1, 0, 1, 1, 1, 4],
       [4, 0, 1, 0, 1, 0, 0, 4],
       [4, 1, 1, 1, 1, 1, 1, 4],
       [4, 4, 4, 4, 4, 4, 4, 4]]
step = 0
da = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i, val in enumerate(dao):
    for x, val1 in enumerate(val):
        if val1 == 0:
            stack = []
            step += 1
            dao[i][x] = 2
            da[step] += 1
            stack.append([i, x])
            print([i, x])

            while len(stack) != 0:  #当栈长度不为0的时候
                a = stack[len(stack) - 1][0]
                b = stack[len(stack) - 1][1]
                if dao[a][b + 1] == 0:
                    da[step] += 1
                    dao[a][b + 1] = 2
                    stack.append([a, b + 1])
                    print([a, b + 1])
                    continue

                if dao[a][b - 1] == 0:
                    da[step] += 1
                    dao[a][b - 1] = 2
                    stack.append([a, b - 1])
                    print([a, b - 1])
                    continue

                if dao[a + 1][b] == 0:
                    da[step] += 1
                    dao[a + 1][b] = 2
                    stack.append([a + 1, b])
                    print([a + 1, b])
                    continue

                if dao[a - 1][b] == 0 :
                    da[step] += 1
                    dao[a - 1][b] = 2
                    stack.append([a - 1, b])
                    print([a - 1, b])
                    continue

                print('后退到' + str(stack.pop()))
print(da)
print(dao)
for i, x in enumerate(da):
    if x != 0:
        print('小岛' + str(i) + '号面积:' + str(x))
