import pandas as pd

# Create transaction set
T = pd.DataFrame({"items":
                 [{"beef", "chicken", "milk"},
                 {"beef", "cheese"},
                 {"cheese", "boots"},
                 {"beef", "chicken", "cheese"},
                 {"beef", "chicken", "clothes", "cheese", "milk"},
                 {"chicken", "clothes", "milk"},
                 {"chicken", "milk", "clothes"}]})

# Minimum support
min_sup = .30

# Initial pass function
def initpass(T):
    C1 = pd.DataFrame(columns=['items', 'count'])

    # Count support of individual items
    for i in range(len(T)):
        for j in T['items'][i]:
            if j in list(C1['items']):
                C1['count'][list(C1['items']).index(j)] += 1
            else:
                C1 = C1.append(pd.Series([j, 1], index=['items', 'count']), ignore_index=True)

    C1 = C1.sort_values('items') # Sort items lexicographically
    return C1

# First pass over T
C1 = initpass(T)
