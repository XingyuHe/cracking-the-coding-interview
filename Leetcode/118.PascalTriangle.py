def generate(n):
    
    ans = []

    if n > 0:
        ans.append([1])
    i = 2
    while i < n + 1:
        
        row_i = [1]
        row_i_1 = ans[i - 2]
        for j in range(1, i - 1):
            row_i.append(row_i_1[j - 1] + row_i_1[j])

        row_i.append(1)
        ans.append(row_i)
        i += 1
        
    return ans 

print generate(5)
