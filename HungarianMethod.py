import pprint

Ans = 10000
rowLine = [0, 0, 0, 0, 0]
colLine = [0, 0, 0, 0, 0]

def rowMin(grid, i, cols):
    res = grid[i][0]
    for j in range(1, cols):
        res = min(grid[i][j], res)
    return res

def colMin(grid, j, rows):
    res = grid[0][j]
    for i in range(1, rows):
        res = min(grid[i][j], res)
    return res

def minLines(i, zeros, row, col, ans):
    if(i == len(zeros)):
        global Ans
        global rowLine
        global colLine

        if(ans < Ans):
            Ans = ans
            for i in range(len(row)):
                rowLine[i] = row[i]
                colLine[i] = col[i]
        return 

    r = zeros[i][0]
    c = zeros[i][1]

    if(row[r] == 1 or col[c] == 1):
        minLines(i + 1, zeros, row, col, ans)
    else:
        row[r] = 1
        minLines(i + 1, zeros, row, col, ans + 1)
        row[r] = 0

        col[c] = 1
        minLines(i + 1, zeros, row, col, ans + 1)
        col[c] = 0

def modifyProblem(grid):
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        minEle = rowMin(grid, i, col)
        if(minEle == 0):
            continue
        for j in range(col):
            grid[i][j] -= minEle
    
    for j in range(col):
        minEle = colMin(grid, j, row)
        if(minEle == 0):
            continue
        for i in range(row):
            grid[i][j] -= minEle
    
    return grid

def findZeros(grid):
    zeros = []
    
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if(grid[i][j] == 0):
                zeros.append([i, j])

    return zeros

def degeneracyModify(grid, row, col):
    n = len(grid)
    m = len(grid[0])

    res  = 10000

    for i in range(n):
        for j in range(m):
            if(row[i] == 0 and col[j] == 0):
                res = min(res, grid[i][j])
    
    for i in range(n):
        for j in range(m):
            if(row[i] == 0 and col[j] == 0):
                grid[i][j] -= res
            if(row[i] == 1 and col[j] == 1):
                grid[i][j] += res

    return grid   

def countZeros(grid, i, size):
    res = 0
    for j in range(size):
        if(grid[i][j] == 0):
            res = res + 1
    return res

def costEstimation(grid, originalGrid):
    row = [0 for _ in range(len(grid))]
    col = [0 for _ in range(len(grid[0]))]

    cost = 0 
    sZ = []
    nZ = []
    for i in range(len(grid)):
        if(countZeros(grid, i, len(grid[0])) == 1):
            sZ.append(i)
        else:
            nZ.append(i)

    for i in sZ:
        for j in range(len(grid[0])):
            if(grid[i][j] == 0 and row[i] == 0 and col[j] == 0):
                cost += originalGrid[i][j]
                row[i] = 1
                col[j] = 1

    for i in nZ:
        for j in range(len(grid[0])):
            flag = 0
            if(grid[i][j] == 0 and row[i] == 0 and col[j] == 0):
                flag = 1
                row[i] = 1
                col[j] = 1
                cost += originalGrid[i][j]
            if(flag == 1):
                break
    return cost

if __name__ == "__main__":

    originalGrid = [[9, 11, 14, 11, 7], [6, 15, 13, 13, 10], [12, 13, 6, 8, 8], [11, 9, 10, 12, 9], [7, 12, 14, 10, 14]]
    grid = [[9, 11, 14, 11, 7], [6, 15, 13, 13, 10], [12, 13, 6, 8, 8], [11, 9, 10, 12, 9], [7, 12, 14, 10, 14]]
    
    grid = modifyProblem(grid)
    zeros = findZeros(grid)
    
    row = [0 for _ in range(len(grid))]
    col = [0 for _ in range(len(grid[0]))]
    
    minLines(0, zeros, row, col, 0)

    while(Ans < len(grid)):
        Ans = len(grid) * len(grid[0])
        grid = degeneracyModify(grid, rowLine, colLine)
        grid = modifyProblem(grid)
        zeros = findZeros(grid)
        minLines(0, zeros, row, col, 0)
    
    cost = costEstimation(grid, originalGrid)
    print("\nThe cost of the allocation: ", cost)