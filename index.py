import time

def weight_of(subset):
    return sum(item["weight"] for item in subset)

def value_of(subset):
    return sum(item["value"] for item in subset)

def bruteForceKnapSack(capacity, items):
    candidates = []

    def getCandidateSubsets(buffer, start):
        addedSomething = False
        for i in range(start, len(items)):
            if weight_of(buffer) + items[i]["weight"] <= capacity:
                buffer.append(items[i])
                getCandidateSubsets(buffer, i + 1)
                buffer.pop()
                addedSomething = True
        if not addedSomething:
            # store a snapshot (copy) of the current subset
            candidates.append(list(buffer))

    getCandidateSubsets([], 0)

    if not candidates:
        return None  # or return ([], 0) depending on what you prefer

    
    best = max(candidates, key=value_of)
    best_value = value_of(best)
    print("Chosen items Brute Force:")
    i = 0
    while i < len(best):
        print("Item #" + str(best[i]["item"]) + " is selected")
        i += 1
    print("best value is " + str(best_value) )
    


def knapSack(capacity, items):
    n = len(items)

    # F[i][j] = max value using items 1..i with capacity j
    F = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Memoization table initialized with -1 except F[0][*] = 0
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            F[i][j] = -1

    def MFKnapsack(i, j):
        if F[i][j] < 0:
            if j < items[i - 1]["weight"]:
                value = MFKnapsack(i - 1, j)
            else:
                value = max(
                    MFKnapsack(i - 1, j),
                    items[i - 1]["value"] + MFKnapsack(i - 1, j - items[i - 1]["weight"])
                )
            F[i][j] = value
        return F[i][j]

    # Fill the table
    MFKnapsack(n, capacity)

    # TRACEBACK
    i, j = n, capacity
    chosen = []

    while i > 0 and j > 0:
        # If value comes from above row, item not taken
        if F[i][j] == F[i - 1][j]:
            i -= 1
        else:
            # Item was taken
            chosen.append(items[i - 1])
            j -= items[i - 1]["weight"]
            i -= 1

    print("Chosen items:")
    for x in chosen:
        print(x)
    i = len(F) - 1
    j = len(F[i]) - 1
    print("There are " + str((j + 1) * (i +1) ) + " stored in dynamic approach")
    print("Best value is " + str(F[i][j]))

    
  
capacity = 250

items = [
    {"item": 1,  "value": 20, "weight": 4},
    {"item": 2,  "value": 18, "weight": 3},
    {"item": 3,  "value": 14, "weight": 2},
    {"item": 4,  "value": 16, "weight": 5},
    {"item": 5,  "value": 40, "weight": 9},

    {"item": 6,  "value": 25, "weight": 7},
    {"item": 7,  "value": 10, "weight": 1},
    {"item": 8,  "value": 12, "weight": 3},
    {"item": 9,  "value": 22, "weight": 6},
    {"item": 10, "value": 28, "weight": 8},

    {"item": 11, "value": 30, "weight": 6},
    {"item": 12, "value": 35, "weight": 10},
    {"item": 13, "value": 40, "weight": 11},
    {"item": 14, "value": 12, "weight": 4},
    {"item": 15, "value": 15, "weight": 5},

    {"item": 16, "value": 7,  "weight": 1},
    {"item": 17, "value": 9,  "weight": 2},
    {"item": 18, "value": 28, "weight": 7},
    {"item": 19, "value": 33, "weight": 9},
    {"item": 20, "value": 26, "weight": 8},

    {"item": 21, "value": 18, "weight": 3},
    {"item": 22, "value": 22, "weight": 6},
    {"item": 23, "value": 27, "weight": 7},
    {"item": 24, "value": 35, "weight": 10},
    {"item": 25, "value": 12, "weight": 2},
]


# print(dt.fromtimestamp())
capacity = 40
t1 = time.time()
knapSack(capacity, items)
t2 = time.time()
print("For Dynamic Programming, " + str((t2 - t1)) + " seconds")

t1 = time.time()
bruteForceKnapSack(capacity, items)
t2 = time.time()
print("For Brute Force, " + str((t2 - t1)) + " seconds")
