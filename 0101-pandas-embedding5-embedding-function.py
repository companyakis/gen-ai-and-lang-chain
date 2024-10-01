# let's create a function to get embedding

# https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

def getting_embeddings(text, model):
    return robot.embeddings.create(
        input = [text],
        model = model
    ).data[0].embedding
