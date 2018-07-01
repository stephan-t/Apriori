import pandas as pd
from itertools import combinations

# Create transaction set
T = pd.DataFrame({"items":
                 [("beef", "chicken", "milk"),
                  ("beef", "cheese"),
                  ("cheese", "boots"),
                  ("beef", "chicken", "cheese"),
                  ("beef", "chicken", "clothes", "cheese", "milk"),
                  ("chicken", "clothes", "milk"),
                  ("chicken", "milk", "clothes")]})

# Minimum support
min_sup = .30


# Initial pass function
def initpass(T):
    C1 = pd.DataFrame(columns=['items', 'count'])

    # Count support of individual items
    for i in range(len(T)):
        for j in T['items'][i]:
            if j in tuple(C1['items']):
                C1['count'][tuple(C1['items']).index(j)] += 1
            else:
                C1 = C1.append(pd.Series([j, 1], index=['items', 'count']), ignore_index=True)

    C1 = C1.sort_values('items')  # Sort items lexicographically
    C1 = C1.reset_index(drop=True)
    return C1


# Apriori algorithm
C1 = initpass(T)  # First pass over T
F1 = C1[C1['count']/len(T) >= min_sup]  # Determine frequent itemsets
F1 = F1.reset_index(drop=True)

# F2 Candidate generation
C2 = pd.DataFrame(columns=['items', 'count'])

for i in range(len(F1)):
    for j in range(i+1, len(F1)):
        # Join two itemsets and add to candidates
        C2 = C2.append(pd.Series([(F1['items'][i], F1['items'][j]), 0],
                                 index=['items', 'count']), ignore_index=True)

# Check if each candidate itemset is in transaction set
for i in range(len(T)):
    for j in range(len(C2)):
        if set(C2['items'][j]).issubset(T['items'][i]):
            C2['count'][j] += 1


# Determine frequent itemsets
F2 = C2[C2['count']/len(T) >= min_sup]
F2 = F2.reset_index(drop=True)



# F3 Candidate generation
C3 = pd.DataFrame(columns=['items', 'count'])

for i in range(len(F2)):
    for j in range(i+1, len(F2)):
        # Find pairs that differ only by last item
        if (F2['items'][i][:-1] == F2['items'][j][:-1]) & (F2['items'][i][-1] != F2['items'][j][-1]):
            # Join two itemsets and add to candidates
            C3 = C3.append(pd.Series([F2['items'][i] + (F2['items'][j][-1],), 0],
                                     index=['items', 'count']), ignore_index=True)

            # Delete candidate if a subset is not in k-1 frequent itemset
            s = tuple(combinations(C3['items'][len(C3)-1], 2))
            if not set(s).issubset(tuple(F2['items'])):
                C3 = C3.drop(C3.index[-1])

# Check if each candidate itemset is in transaction set
for i in range(len(T)):
    for j in range(len(C3)):
        if set(C3['items'][j]).issubset(T['items'][i]):
            C3['count'][j] += 1


# Determine frequent itemsets
F3 = C3[C3['count']/len(T) >= min_sup]
F3 = F3.reset_index(drop=True)
