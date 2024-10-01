# https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken

def calculate_number_of_tokens(text: str, encoding_name: str) -> int:
    import tiktoken as tk
    encoding = tk.get_encoding(encoding_name)
    number_of_tokens = len(encoding.encode(text))
    return number_of_tokens

token_1 = calculate_number_of_tokens("A barking dog never bites", "cl100k_base")

print(token_1) # 6

token_2 = calculate_number_of_tokens("Ceteris paribus", "p50k_base")

print(token_2) # 5
