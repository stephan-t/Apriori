from itertools import combinations
from apriori import candidate_gen
import pandas as pd


# Association rule generation algorithm
def rule_gen(T, F, min_conf):
    for i in range(2, len(F)):  # Start from frequent 2-itemsets
        for j in range(len(F[i])):
            f = F[i].loc[j, ['items', 'count']]  # Frequent k-itemset (f[0] = itemset, f[1] = count)
            con = tuple(combinations(f[0], 1))  # Generate 1-item consequents

            for c in con:
                ant = tuple(sorted(set(f[0]) - set(c)))  # Association rule antecedents
                ant_cnt = int(F[len(ant)]['count'][F[len(ant)]['items'] == ant])  # Antecedent support count

                if f[1] / ant_cnt >= min_conf:
                    # Output association rules meeting minimum confidence
                    print(str(ant) + " -> " + str(c) + " [sup = " + str(f[1]) + "/" + str(len(T)) +
                          ", conf = " + str(f[1]) + "/" + str(ant_cnt) + "]")

                    # Store 1-item consequents meeting minimum confidence
                    if 'H' not in globals():
                        H = {1: pd.DataFrame(pd.Series((c,)), columns=['items'])}
                    else:
                        H[1] = H[1].append(pd.Series((c,), index=['items']), ignore_index=True)

                    rule_gen_all(T, F, f, H, 1, min_conf)  # Generate all rules from 1-item consequents


# Generate all rules procedure
def rule_gen_all(T, F, f, H, m, min_conf):
    if (len(f[0]) > m + 1) and (not H[m].empty):
        H = candidate_gen(H, m)  # Generate consquent supersets

        for h in H[m + 1]['items']:
            ant = tuple(set(f[0]) - set(h))  # Association rule antecedents
            ant_cnt = int(F[len(ant)]['count'][F[len(ant)]['items'] == ant])  # Antecedent support count
            conf = f[1] / ant_cnt  # Confidence of rule with (m + 1)-item consequents

            if conf >= min_conf:
                # Output association rules meeting minimum confidence
                print(str(ant) + " -> " + str(h) + " [sup = " + str(f[1]) + "/" + str(len(T)) +
                      ", conf = " + str(f[1]) + "/" + str(ant_cnt) + "]")
            else:
                # Delete consequents not meeting minimum confidence
                H[m + 1] = H[m + 1].drop(H[m + 1].index[-1])

        rule_gen_all(T, F, f, H, m + 1, min_conf)  # Generate all rules from (m + 1)-item consequents
