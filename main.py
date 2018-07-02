from apriori import apriori
from ast import literal_eval
import pandas as pd

# Request filename from user
file = input("Please enter dataset filename: ")

# Read transaction dataset
T = pd.read_csv(file)

# Preprocess data
T = T.iloc[:, [1]]
for i in range(len(T)):
    T.iloc[:, 0][i] = tuple(T.iloc[:, 0][i].replace(" ", "").split(','))

# Request minimum support from user
min_sup = input("Please enter a minimum support: ")

# Validate input
while True:
    try:
        min_sup = literal_eval(min_sup)
    except (ValueError, SyntaxError):
        min_sup = input("Please enter a valid number: ")
        continue

    if min_sup <= 0:
        min_sup = input("Please enter a positive number: ")
        continue

    if type(min_sup) == int:
        if min_sup > len(T):
            min_sup = input("Please enter a number less than or equal to " + str(len(T)) + ": ")
            continue
        else:
            min_sup /= len(T)
            break
    elif type(min_sup) == float:
        if min_sup > 1.0:
            min_sup = input("Please enter a number less than or equal to 1.0: ")
            continue
        else:
            break

# Output all frequent itemsets
F = apriori(T, min_sup)
print("Frequent itemsets: \n", F)
