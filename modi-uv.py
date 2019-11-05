import numpy as np
from math import isnan

def get_an_occupied_cell(allocs, i, j):
    try:
        if (allocs[i][j + 1] != 0):
            return i, j+1
    except IndexError:
        pass
    try:
        if (allocs[i+1][j] != 0):
            return i+1, j
    except IndexError:
        pass
    try:
        if (allocs[i-1][j] != 0):
            return i-1, j
    except IndexError:
        pass
    try:
        if (allocs[i][j-1] != 0):
            return i, j-1
    except IndexError:
        pass
    return -1, -1

def create_cycle(allocs, neg_i, neg_j):
    cycle_coordinates = []
    i, j = get_an_occupied_cell(allocs, neg_i, neg_j)
    print("@", i, j)
    while i != neg_i or j != neg_j:
        if i == -1 or j == -1:
            raise Exception("Couldn't find another cell")
        cycle_coordinates.append((i, j))
        i, j = get_an_occupied_cell(allocs, i, j)
    print("%", cycle_coordinates)
    return cycle_coordinates

def get_min_in_cycle(allocs, cycle_coordinates):
    min = 0
    for i in cycle_coordinates:
        if min > allocs[i[0]][i[1]]:
            min = allocs[i[0]][i[1]]
    return min

def modify_cycle(allocs, cycle_coordinates):
    t = 1
    min = get_min_in_cycle(allocs, cycle_coordinates)
    for x, y in cycle_coordinates:
        allocs[x][y] = min + int(t * allocs[x][y])
        if t == 1:
            t = -1
        else:
            t = 1

def get_all_allocated_coordinates(allocs):
    coordinates = []
    for i in range(len(allocs)):
        for j in range(len(allocs[0])):
            if allocs[i][j] > 0:
                coordinates.append((i, j))
    return coordinates

def isAnyNan(l):
    for i in l:
        if isnan(i):
            return True
    return False

def get_uv(costs, allocs):
    u = []
    v = []

    for _ in costs:
        u.append(float('nan'))
    for _ in costs[0]:
        v.append(float('nan'))
    
    u[0] = 0
    coordinates = get_all_allocated_coordinates(allocs)
    stopLoopCount = 0
    while isAnyNan(u) or isAnyNan(v):
        stopLoopCount += 1
        for x, y in coordinates:
            if not isnan(u[x]) and isnan(v[y]):
                v[y] = costs[x][y] - u[x]
            elif isnan(u[x]) and not isnan(v[y]):
                u[x] = costs[x][y] - v[y]
        if stopLoopCount % 100 == 0:
            ans = input("Loop ran for {0} times. Do you want to continue? [y] ".format(stopLoopCount))
            if ans != 'y':
                break
    return u, v

def isValid(costs, allocs, u, v):
    min_val = 1000000000000000
    min_x = -1
    min_y = -1
    #print(u, v)
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            if allocs[i][j] == 0:
                x = costs[i][j] - u[i] - v[j]
                #print('#', x, i, j)
                if x < min_val:
                    min_val = x
                    min_x, min_y = i, j
    if (min_val < 0):
        return min_x, min_y
    else:
        return -1, -1

def tot_cost(alloc, cost, m, n):
    t_cost = 0

    for i in range(m):
        for j in range(n):
            t_cost += alloc[i][j] * cost[i][j]
    return t_cost


if __name__ == '__main__':
    costs = []
    allocs = []
    rows_count = int(input("Enter rows: "))
    
    print("Enter the cost matrix: ")
    for i in range(rows_count):
        costs.append(list(map(int, input().strip().split(' '))))
    
    print("Enter the allocation matrix: ")
    for i in range(rows_count):
        allocs.append(list(map(int, input().strip().split(' '))))

    u, v = get_uv(costs, allocs)
    x, y = isValid(costs, allocs, u, v)
    while x != -1 and y != -1:
        cycle_coordinates = create_cycle(allocs, x, y)
        modify_cycle(allocs, cycle_coordinates)
        print("  ##  ")
        print(u, v)
        print(x, y)
        print(cycle_coordinates)
        print(allocs)
        print("  ##  ")
        ans = input("Continue? [y]")
        if ans != 'y':
            break
        u, v = get_uv(costs, allocs)
        x, y = isValid(costs, allocs, u, v)

    print("\nOptimal solution: ")
    print(np.array(allocs))
    print("Min. cost: ", tot_cost(allocs, costs, rows_count, len(costs[0])))