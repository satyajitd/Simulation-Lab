import numpy as np 

def min_row(mat, row, n, penality_col):
    idx = -1
    val = 100000
    for i in range(n):
        if mat[row][i] < val and penality_col[i] != -1:
            val = mat[row][i]
            idx = i
    return idx

def min_2_row(mat, row, n, min_idx, penality_col):
    idx = -1
    val = 100000
    for i in range(n):
        if mat[row][i] <= val and i != min_idx and penality_col[i] != -1:
            val = mat[row][i]
            idx = i
    return idx

def min_col(mat, col, m, penality_row):
    idx = -1
    val = 100000
    for i in range(m):
        if mat[i][col] < val and penality_row[i] != -1:
            val = mat[i][col]
            idx = i
    return idx

def min_2_col(mat, col, m, min_idx, penality_row):
    idx = -1
    val = 100000
    for i in range(m):
        if mat[i][col] <= val and i != min_idx and penality_row[i] != -1:
            val = mat[i][col]
            idx = i
    return idx

def max_p(penality):
    idx = 0
    val = penality[0]

    for i in range(1, len(penality)):
        if val < penality[i]:
            idx = i
            val = penality[i]
    return idx 

def tot_cost(alloc, cost, m, n):
    t_cost = 0

    for i in range(m):
        for j in range(n):
            t_cost += alloc[i][j] * cost[i][j]
    return t_cost

if __name__ == "__main__":
    
    print("Enter no. of sources and destinations: ")
    m, n = input().strip().split(' ')
    m = int(m)
    n = int(n)

    mat = np.zeros((m,n))
    alloc = np.zeros((m,n))

    print("Enter cost matrix: ")
    for i in range(m):
        for j in range(n):
            mat[i][j] = int(input())

    demand = []
    t_sum = 0
    print("Enter the demand: ")
    for i in range(n):
        demand.append(int(input()))
        t_sum += demand[i]

    supply = []
    print("Enter the supply: ")
    for i in range(m):
        supply.append(int(input()))
        t_sum -= supply[i]
    
    if t_sum != 0:
        print("Unbalanced problem")
        exit()
    
    penality_row = [0 for _ in range(m)]
    penality_col = [0 for _ in range(n)]

    loop = m + n - 1
    while(loop):
        # row
        for i in range(m):
            if penality_row[i] == -1:
                continue
            
            min_idx = min_row(mat, i, n, penality_col)
            min_2_idx = min_2_row(mat, i, n, min_idx, penality_col)
            
            if min_2_idx == -1:
                penality_row[i] =  mat[i][min_idx]
            else:
                penality_row[i] = mat[i][min_2_idx] - mat[i][min_idx]
        
        # column
        for j in range(n):
            if penality_col[j] == -1:
                continue

            min_idx = min_col(mat, j, m, penality_row)
            min_2_idx = min_2_col(mat, j, m, min_idx, penality_row)

            if min_2_idx == -1:
                penality_col[j] = mat[min_idx][j]
            else:
                penality_col[j] = mat[min_2_idx][j] - mat[min_idx][j]
        
        r_p = max_p(penality_row)
        c_p = max_p(penality_col)

        if(penality_row[r_p] >= penality_col[c_p]):
            r_min = min_row(mat, r_p, n, penality_col)
            alloc[r_p][r_min] = min(supply[r_p], demand[r_min])
            supply[r_p] -= alloc[r_p][r_min]
            demand[r_min] -= alloc[r_p][r_min]

            if supply[r_p] == 0:
                penality_row[r_p] = -1
            elif demand[r_min] == 0:
                penality_col[r_min] = -1
                
        else:
            c_min = min_col(mat, c_p, m, penality_row)
            alloc[c_min][c_p] = min(supply[c_min], demand[c_p])
            supply[c_min] -= alloc[c_min][c_p]
            demand[c_p] -= alloc[c_min][c_p]

            if supply[c_min] == 0:
                penality_row[c_min] = -1
            elif demand[c_p] == 0:
                penality_col[c_p] = -1
        
        loop -= 1

    print("Allocation made: ")
    print(alloc)
    print("Min. cost: ", tot_cost(alloc, mat, m, n))