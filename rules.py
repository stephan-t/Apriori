from itertools import combinations
from apriori import candidate_gen
import pandas as pd

# Association rule generation algorithm
def rule_gen(T, F, min_conf):
    for i in range(2, len(F)):  # Start from frequent 2-itemsets
        for j in range(len(F[i])):
            con = tuple(combinations(F[i]['items'][j], 1))  # Association rule consequents (1-item subsets)
            for c in con:

                ant = tuple(set(F[i]['items'][j]) - set(c))  # Association rule antecedents
                l = len(ant)  # Antecedent itemset size
                ant = tuple(sorted(ant))
                ant_cnt = int(F[l]['count'][F[l]['items'] == ant])  # Antecedent support count
                f_cnt = F[i]['count'][j]  # Frequent itemset support count

                # Output association rules meeting minimum confidence
                if f_cnt/ant_cnt >= min_conf:
                    print(str(ant) + " -> " + str(c) + " [sup = " + str(f_cnt) + "/" + str(len(T)) +
                                                          ", conf = " + str(f_cnt) + "/" + str(ant_cnt) + "]")

                    # Store 1-item consequents
                    if not 'H' in locals():
                        H = {1: pd.DataFrame(pd.Series((c,)), columns=['items'])}
                    else:
                        H[1] = H[1].append(pd.Series((c,), index=['items']), ignore_index=True)

                    f = F[i].loc[j, ['items','count']]  # Frequent k-itemset
                    ap_rule_gen(f, H, 1)  # Generate all rules from 1-item consequents


# All rule generation procedure
def all_rule_gen(f, H, m):  # H_m is set of m-item consequents
    k = len(f)  # Frequent itemset size
    if k > m + 1 and H[m] != ((),):
        H = candidate_gen(H, m)

