import chromadb
from pprint import pprint

# Create document collection. Collections are where we store our embeddings,
#  documents, and any additional metadata.

client = chromadb.Client()

# collection = client.create_collection("all-my-documents")

collection = client.create_collection(
      name="all-my-documents",
      metadata={"hnsw:space": "cosine"} # metadata is optional
  )

# we can store our text, and handle tokenization, embedding, and indexing automatically! 
# Chroma will also store the documents themselves. If the documents are too large to embed 
# using the chosen embedding function, an exception will be raised.


# By default, Chroma uses the Sentence Transformers all-MiniLM-L6-v2 model to create embeddings.
collection.add(
    documents=[
        "This is a document about food",
        "This is a document about animal's food",
        "This is a document about cats and dogs",
    ],
    metadatas=[{"topic": "food"}, {"topic": "animal"}, {"topic": "animal"}],
    ids=["doc1", "docs2", "doc3"],
)

results = collection.query(
    query_texts=["This is a query asking about pizza"],
    n_results=2,
)

