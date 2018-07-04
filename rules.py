from itertools import combinations

# Minimum confidence
min_conf = .80

# Generate association rules
# for i in range(len(F), 1, -1):  # Go from largest to size 2 frequent itemsets
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
