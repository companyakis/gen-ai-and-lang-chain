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

df = df[df.number_of_tokens <= max_token]

# let's create a function to get embedding

# https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

def getting_embeddings(text, model):
    return robot.embeddings.create(
        input = [text],
        model = model
    ).data[0].embedding
    
df["embedding"] = df["txt_combined"].apply(lambda i: getting_embeddings(i, model="text-embedding-ada-002"))

print(df[["txt_combined", "embedding"]])

"""
                                        txt_combined                                          embedding
0             service is too bad I'll never go again  [-0.01820586435496807, -0.007881726138293743, ...
1                     i like it yes I'll visit again  [-0.003247889457270503, -0.006252884864807129,...
2  the place is too dirty disgusting place... I w...  [-0.001408501761034131, -0.01490306667983532, ...

"""
