# Apriori-Python

## Description
This is an implementation of the Apriori algorithm in Python which generates frequent itemsets and association rules from transactional datasets.

## Requirements
- [pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)

## Usage
1. Put dataset file in "data" folder
2. Run: `python "[path to program]\main.py"`
3. Enter dataset filename
4. Enter minimum support
5. Enter minimum confidence
6. Results are printed to console


## Datasets
- groceries.csv: provided by Michael Hahsler, Kurt Hornik and Thomas Reutterer in the arules R package
- groceries_small.csv: provided by Bing Liu in Web Data Mining
  
## References
- Implementation is based on the pseudocode written by Bing Liu in Web Data Mining
[[1]](https://books.google.ca/books?id=jnCi0Cq1YVkC&lpg=PP1&pg=PA21#v=onepage&q&f=false)
[[2]](https://books.google.ca/books?id=jnCi0Cq1YVkC&lpg=PP1&pg=PA25#v=onepage&q&f=false)
- The original Apriori algorithm was proposed by Rakesh Agrawal and Ramakrishnan Srikant in their paper ["Fast algorithms for mining association rules"](http://www.vldb.org/conf/1994/P487.PDF)
