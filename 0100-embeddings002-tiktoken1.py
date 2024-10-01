# https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken

import tiktoken as tk

encoding = tk.get_encoding("r50k_base")

print(encoding.encode("Always keep it simple")) # [30374, 1394, 340, 2829]

print(encoding.decode([30374, 1394, 340, 2829])) # Always keep it simple
