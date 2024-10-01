import pandas as pd

df = pd.read_csv("fakedata.csv")

df["txt_combined"] = df.review.str.strip() + " " + df.final.str.strip()

print(df.txt_combined[0])  # servise is too bad I'll never go again



