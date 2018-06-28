import pandas as pd

# Create transaction set
T = pd.DataFrame({"Items":
                 [{"Beef", "Chicken", "Milk"},
                 {"Beef", "Cheese"},
                 {"Cheese", "Boots"},
                 {"Beef", "Chicken", "Cheese"},
                 {"Beef", "Chicken", "Clothes", "Cheese", "Milk"},
                 {"Chicken", "Clothes", "Milk"},
                 {"Chicken", "Milk", "Clothes"}]})
