from apriori import apriori
from rules import rule_gen
from validate import validate_input
import pandas as pd

# Request filename from user
file = input("Please enter dataset filename: ")

# Read transaction dataset
T = pd.read_csv(file)

# Preprocess data
T = T.iloc[:, [1]]
for i in range(len(T)):
    T.iloc[:, 0][i] = tuple(T.iloc[:, 0][i].replace(" ", "").split(","))

# Request minimum support from user
min_sup = input("Please enter a minimum support between 0.0-1.0 or 1-" + str(len(T)) + ": ")
min_sup = validate_input(min_sup, T)

# Request minimum support from user
min_conf = input("Please enter a minimum confidence between 0.0-1.0: ")
min_conf = validate_input(min_conf)

# Output all frequent itemsets
F = apriori(T, min_sup)
print("Frequent itemsets: \n", F, "\n")

# Output all association rules
print("Association rules:")
rule_gen(T, F, min_conf)
