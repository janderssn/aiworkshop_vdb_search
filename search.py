from vdb import find_most_similar_embeddings
from embed import encode_string

query = "A black jersey"

query_embedding = encode_string(query)

results = find_most_similar_embeddings(query_embedding, n_results=3)

print(results)

ids = results["ids"][0]
dists = results["distances"][0]
metadatas = results["metadatas"][0]