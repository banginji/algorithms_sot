def lev_distance(str1,str2):
    str1_length = len(str1)
    str2_length = len(str2)

    cost_table = [[0 for _ in range(str1_length+1)] for _ in range(str2_length+1)]

    for i in range(1, str1_length+1):
        cost_table[0][i] = i

    for j in range(1, str2_length+1):
        cost_table[j][0] = j

    for j in range(1, str2_length+1):
        for i in range(1, str1_length+1):
            cost = 0 if str1[i-1] == str2[j-1] else 1
            cost_table[i][j] = min(cost_table[i-1][j] + 1, cost_table[i][j-1] + 1, cost_table[i-1][j-1] + cost)
    return cost_table[str1_length][str2_length]


if __name__ == '__main__':
    print(lev_distance("paled", "palew"))
