from langchain_openai.embeddings import OpenAIEmbeddings
from src.utils import get_openai_api_key
from sklearn.metrics.pairwise import cosine_similarity

embeddings = OpenAIEmbeddings()
output = embeddings.embed_query('You are boring')
output2 = embeddings.embed_query('I think kashish is very boring')
output3 = embeddings.embed_query('My phone is almost fully charged')
print(cosine_similarity([output], [output2])[0][0])
print(cosine_similarity([output], [output3])[0][0])

class GenerateEmbeddings():
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        
    def create(self, blob:str):
        return self.embeddings.embed_query(blob)
    
    def create_docs(self, docs:dict):
        