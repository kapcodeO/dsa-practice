strs = ["bat", "bag", "bank", "bad"]

idx = 0
while idx < len(strs):
    for i in range(len(strs[0])):
        if i < len(strs[i]):
            print(strs[i][idx], end=" ")
    print()
    idx += 1
