import numpy as np

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

    i = 0
    j = 0

    allocations = np.zeros((sources, destins))
    tot_cost = 0

    while(i < sources and j < destins):
        allocate = min(supply[i], demand[j])
        allocations[i][j] = allocate
        supply[i] = supply[i] - allocate
        demand[j] = demand[j] - allocate

        tot_cost = tot_cost + allocate*cost[i][j]

        if supply[i] == 0:
            i = i + 1
        elif demand[j] == 0:
            j = j + 1

    print("Allocations made: ")
    print(allocations)

    print("Total cost of allocations: ", tot_cost)