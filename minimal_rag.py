from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
   
# small knowledge base of sentences
docs = [
    "Christopher Nolan directed Inception in 2010.",
    "Inception starred Leonardo DiCaprio.",
    "Christopher Nolan was born in London, UK.",
    "Leonardo DiCaprio was born in Los Angeles, USA."
]

# index documents
encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
doc_embeddings = encoder.encode(docs)

index = faiss.IndexFlatIP(384)  # 384-Dimension vector embedding so it can be compared to documents.
faiss.normalize_L2(doc_embeddings)
index.add(doc_embeddings)

# retrieve
query = "Where was the director of Inception born?"
query_emb = encoder.encode([query])
faiss.normalize_L2(query_emb)

distances, indices = index.search(query_emb, k=4)
retrieved_docs = [docs[i] for i in indices[0]]

print("Retrieved:")
for doc in retrieved_docs:
    print(f"  - {doc}")

# generate (mock for now)
context = "\n".join(retrieved_docs)
print(f"\nPrompt: {query}\nContext: {context}")