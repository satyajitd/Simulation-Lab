import numpy as np

def find_min(allocations, cost, supply, demand):
    A_i = -1
    A_j = -1
    min_cost = 100000
    allocate = 0

    for i in range(len(supply)):
        for j in range(len(demand)):
            if demand[j] == 0 or supply[i] == 0 or allocations[i][j] != 0:
                continue
            if cost[i][j] < min_cost:
                min_cost = cost[i][j]
                A_i = i
                A_j = j
                allocate = min(supply[i], demand[j])
            elif cost[i][j] == min_cost and allocate < min(supply[i], demand[j]):
                allocate = min(supply[i], demand[j])
                A_i = i
                A_j = j  

    return [A_i, A_j]

if __name__ == "__main__":
    
    print("Enter the number of sources: ")
    sources = int(input().strip())

    print("Enter the number of destinations: ")
    destins = int(input().strip())

    cost = np.zeros((sources, destins))

    print("Enter the cost matrix: ")
    for i in range(sources):
        for j in range(destins):
            cost[i][j] = int(input().strip())

    supply = []
    demand = []

    tot_supply = 0
    tot_demand = 0

    print("Enter the supply capacaties: ")
    for i in range(sources):
        supply.append(int(input().strip()))
        tot_supply = tot_supply + supply[i]

    print("Enter the demands: ")
    for j in range(destins):
        demand.append(int(input().strip()))
        tot_demand = tot_demand + demand[j]
            
    if tot_demand != tot_supply:
        print("The model is not balanced!")
        exit()

    allocations = np.zeros((sources, destins))
    tot_cost = 0

    while tot_demand > 0 and tot_supply > 0:
        idx = find_min(allocations, cost, supply, demand)
        allocations[idx[0]][idx[1]] = min(supply[idx[0]], demand[idx[1]])
        tot_cost = tot_cost + allocations[idx[0]][idx[1]]*cost[idx[0]][idx[1]]

        supply[idx[0]] = supply[idx[0]] - allocations[idx[0]][idx[1]]
        demand[idx[1]] = demand[idx[1]] - allocations[idx[0]][idx[1]]
        tot_demand = tot_demand - allocations[idx[0]][idx[1]]
        tot_supply = tot_supply - allocations[idx[0]][idx[1]]

    print("Allocations: ")
    print(allocations)

    print("Total cost of allocation: ", tot_cost)