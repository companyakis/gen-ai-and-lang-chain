# we can filter if we want (max_token = 100 )

from dotenv import load_dotenv

load_dotenv() # use 'override=True' if there are diff keys

from openai import OpenAI

robot = OpenAI()

import pandas as pd

import tiktoken as tk

df = pd.read_csv("fakedata.csv")

df["txt_combined"] = df.review.str.strip() + " " + df.final.str.strip()

max_token = 100 

encoding = tk.get_encoding("cl100k_base")

df["number_of_tokens"] = df["txt_combined"].apply(lambda i: len(encoding.encode(i)))

# we can filter if we want (max_token = 100 )

df = df[df.number_of_tokens <= max_token]

print(df)

"""
    id                  review                                  final                                       txt_combined  number_of_tokens
0  101      service is too bad                    I'll never go again             service is too bad I'll never go again                 9
1  108               i like it                   yes I'll visit again                     i like it yes I'll visit again                 8
2  146  the place is too dirty   disgusting place... I won't go again  the place is too dirty disgusting place... I w...                13

"""
