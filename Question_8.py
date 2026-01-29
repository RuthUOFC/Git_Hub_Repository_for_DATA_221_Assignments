import pandas as pd

data = {
    "A": [1,2,2,1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
#creating the data frame
df = pd.DataFrame(data)

#deriving a new column based on previous ones
df["D"] = (df["A"] * df["B"] + df["C"])

print(df)