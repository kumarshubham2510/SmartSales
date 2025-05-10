import chromadb
from DataExtraction import slides
import pprint

chroma_client = chromadb.Client()

def createVectorData(query,no_results):
    ids_list=[]
    for key,value in slides.items():
        ids_list.append(str(key))

    collection = chroma_client.create_collection(name="my_collection")


    collection.add(
        documents=[value.get_text() for key,value in slides.items()],
        ids=ids_list
    )

    query_results = collection.query(
        query_texts=[query], # Chroma will embed this for you
        n_results=no_results # how many results to return
    )

    return query_results["ids"][0]


results=createVectorData("Advantages Of AI",4)


