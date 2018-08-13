import pandas as pd

tbl = pd.DataFrame([["A","B","C","D","E"],["F","G","H","I","J"],
                    ["K","L","M","N","O"],["P","Q","R","S","T"],
                    ["U","V","W","X","Y"]])

print(tbl)
print("-"*16)
print(tbl.T)