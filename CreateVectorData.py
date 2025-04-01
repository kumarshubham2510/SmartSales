import chromadb
from main import slides
import pprint


chroma_client = chromadb.Client()


collection = chroma_client.create_collection(name="my_collection")


collection.add(
    documents=[x for x in slides],
    ids=[f"id{x}" for x in range(len(slides))]

)

results = collection.query(
    query_texts=["Disadvantages of AI"], # Chroma will embed this for you
    n_results=3 # how many results to return
)

print(results)





