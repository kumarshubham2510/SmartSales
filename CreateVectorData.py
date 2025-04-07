import chromadb
from main import slides
import pprint

chroma_client = chromadb.Client()


ids_list=[]
for key,value in slides.items():
    ids_list.append(str(key))


collection = chroma_client.create_collection(name="my_collection")


collection.add(
    documents=[value.get_text() for key,value in slides.items()],
    ids=ids_list
)

query_results = collection.query(
    query_texts=["What are Anti-virus"], # Chroma will embed this for you
    n_results=3 # how many results to return
)

results=query_results["ids"][0]
# pprint.pprint(query_results)






