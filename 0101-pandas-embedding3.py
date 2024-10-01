import pandas as pd

import tiktoken as tk

df = pd.read_csv("fakedata.csv")

df["txt_combined"] = df.review.str.strip() + " " + df.final.str.strip()

max_token = 100 

encoding = tk.get_encoding("cl100k_base")

df["number_of_tokens"] = df["txt_combined"].apply(lambda i: len(encoding.encode(i)))

print(df[["txt_combined", "number_of_tokens"]])

"""
                                        txt_combined  number_of_tokens
0             service is too bad I'll never go again                 9
1                     i like it yes I'll visit again                 8
2  the place is too dirty disgusting place... I w...                13

"""
