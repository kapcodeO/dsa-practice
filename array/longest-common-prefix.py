strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]

def longest_common_prefix(strs):
    result = ""
    i = 0
    while i >=0:
        flag = True
        for j in range(len(strs)):
            if i < len(strs[j]) and i < len(strs[0][:i+1]):
                if strs[j][i] != strs[0][i]:
                    flag = False
                    break
        if flag:
            result += strs[0][i]
            print(result, i)
        i += 1
         
longest_common_prefix(strs)
