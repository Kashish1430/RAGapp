from langchain_openai.embeddings import OpenAIEmbeddings
from src.utils import get_openai_api_key, get_files_path
from sklearn.metrics.pairwise import cosine_similarity
from src.Database.document_loader import DocumentLoader
import pickle
import os

class GenerateEmbeddings():
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        
    def create(self, blob:str):
        return self.embeddings.embed_query(blob)
    
    def create_docs(self, docs:dict):
        for doc, pages in docs.items():
            for page in pages:
                page.embedding = self.create(page.page_content)
        return docs
    
    def save_obj(self, doc: dict, filepath: str):
        with open(filepath, 'wb') as f:
            pickle.dump(doc, f)
            print('Saving the data done')
    
    def load_obj(self, filepath):
        with open(filepath, 'rb') as f:
            docs = pickle.load(f)
            print("Pickle obj loaded")
        return docs

if __name__ == '__main__':
    doc_loader = DocumentLoader()
    embedd = GenerateEmbeddings()
    all_docs = doc_loader.load_all_docs(doc_loader.books)
    all_docs = embedd.create_docs(all_docs)
    embedd.save_obj(all_docs, 'embeddings.pkl')
    all_docs = embedd.load_obj('embeddings.pkl')
    print(all_docs.keys())
    print(next(iter(all_docs.keys())))
    print(type(all_docs[next(iter(all_docs.keys()))][0].embedding))
    print(all_docs[next(iter(all_docs.keys()))][0].metadata)
    