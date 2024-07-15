from langchain_openai.embeddings import OpenAIEmbeddings
from src.utils import get_openai_api_key, get_files_path
from sklearn.metrics.pairwise import cosine_similarity
from src.Database.document_loader import DocumentLoader

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
        for page in docs[next(iter(docs.keys()))]:
            page.embedding = self.create(page.page_content)
        return docs
    
if __name__ == '__main__':
    doc_loader = DocumentLoader()
    embedd = GenerateEmbeddings()
    all_docs = doc_loader.load_all_docs(doc_loader.books)
    all_docs = embedd.create_docs(all_docs)
    print(all_docs[next(iter(all_docs.keys()))][0])