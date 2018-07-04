from itertools import combinations
import pandas as pd


# Initial pass function
def init_pass(T):
    C = {1: pd.DataFrame(columns=['items', 'count'])}

    # Count support of individual items
    for i in range(len(T)):
        for j in range(len(T['items'][i])):
            if {(T['items'][i][j],)}.issubset(tuple(C[1]['items'])):
                C[1]['count'][tuple(C[1]['items']).index(((T['items'][i][j]),))] += 1
            else:
                C[1] = C[1].append(pd.Series([(T['items'][i][j],), 1],
                                             index=['items', 'count']), ignore_index=True)

    C[1] = C[1].sort_values('items')  # Sort items lexicographically
    C[1] = C[1].reset_index(drop=True)
    return C


# Candidate generation function
def candidate_gen(F, k):
    C = {k: pd.DataFrame(columns=['items', 'count'])}

    for i in range(len(F[k - 1])):
        for j in range(i + 1, len(F[k - 1])):
            # Find pairs that differ only by last item
            if (F[k - 1]['items'][i][:-1] == F[k - 1]['items'][j][:-1]) & \
                    (F[k - 1]['items'][i][-1] != F[k - 1]['items'][j][-1]):
                # Join two itemsets and add to candidates
                C[k] = C[k].append(pd.Series([(F[k - 1]['items'][i]) + (F[k - 1]['items'][j][-1],), 0],
                                             index=['items', 'count']), ignore_index=True)

                # Delete candidate if a subset is not in k-1 frequent itemset
                s = tuple(combinations(C[k]['items'][len(C[k]) - 1], len(C[k]['items'][0]) - 1))
                if not set(s).issubset(tuple(F[k - 1]['items'])):
                    C[k] = C[k].drop(C[k].index[-1])
    return C


# Apriori algorithm
def apriori(T, min_sup):
    C = init_pass(T)  # First pass over T
    F = {1: C[1][C[1]['count'] / len(T) >= min_sup]}  # Determine frequent itemsets
    F[1] = F[1].reset_index(drop=True)

    # Subsequent passes over T
    k = 2
    while not F[k - 1].empty:
        C = candidate_gen(F, k)

        # Check if each candidate itemset is in transaction dataset
        for i in range(len(T)):
            for j in range(len(C[k])):
                if set(C[k]['items'][j]).issubset(T['items'][i]):
                    C[k]['count'][j] += 1  # Count support of candidate itemset

        # Determine frequent itemsets
        F[k] = C[k][C[k]['count'] / len(T) >= min_sup]
        F[k] = F[k].reset_index(drop=True)

        k += 1
    return F
