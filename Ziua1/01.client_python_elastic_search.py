import os
from elasticsearch import Elasticsearch

client = Elasticsearch(
    "http://localhost:9200"
)

# Crearea unui index nou
# client.indices.create(index="python_index")

# Crearea unui nou document in indexul python_index
# client.index(
#     index="python_index",
#     id="112",
#     document={
#         "foo": "foo",
#         "bar": "bar",
#     }
# )

## Citirea unui anumit document
response = client.get(index="python_index", id="112")
print(response)

from pprint import pprint
pprint(response.body)
