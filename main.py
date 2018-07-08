from apriori import apriori
from rules import rule_gen
import validate as vd
import time



# Request filename from user
file = input("Please enter a dataset filename: ")
T = vd.validate_file(file)

# Preprocess data
T['items'] = T['items'].str.replace(", ", ",").str.split(",")
T['items'] = T['items'].apply(tuple)

# Request minimum support from user
min_sup = input("Please enter a minimum support between 0.0-1.0 or 1-" + str(len(T)) + ": ")
min_sup = vd.validate_measure(min_sup, T)

# Request minimum support from user
min_conf = input("Please enter a minimum confidence between 0.0-1.0: ")
min_conf = vd.validate_measure(min_conf)

# Output all frequent itemsets
start_time = time.time()
F = apriori(T, min_sup)
print("\nFrequent itemsets: \n", F)
print("--- %s seconds ---" % round(time.time() - start_time, 3))

# Output all association rules
start_time = time.time()
print("\nAssociation rules:")
rule_gen(T, F, min_conf)
print("--- %s seconds ---" % round(time.time() - start_time, 3))
