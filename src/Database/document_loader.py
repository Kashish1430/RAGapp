from langchain_community.document_loaders import PyPDFLoader
from src.utils import get_files_path
from dataclasses import dataclass

class DocumentLoader():
    def __init__(self):
        self.books = get_files_path('Books')
        
    def __len__(self):
        return len(self.books)
    
    def load_doc(self, doc):
        return PyPDFLoader(doc).load()
    
    def combine_metadata(self, metadata):
        return f"{metadata['source']} - Page {metadata['page']}"
    
    def load_all_docs(self, books):
        document_dict = {}
        for book in books:
            loader = PyPDFLoader(book)
            chapters = loader.load()
            for chapter in chapters:
                chapter.metadata = self.combine_metadata(chapter.metadata)
            document_dict[book] = chapters
        return document_dict
    
if __name__ == '__main__':
    doc_loader = DocumentLoader()
    print(doc_loader.books)
    print(doc_loader.books[0])
    print(len(doc_loader))
    #print(doc_loader.load_doc(doc_loader.books[0]))
    
    all_docs = doc_loader.load_all_docs(doc_loader.books)
    print(all_docs.keys())
    
    print(len(all_docs[next(iter(all_docs.keys()))]))
    
    print(all_docs[next(iter(
        all_docs.keys()))][0].page_content)
    
    print(all_docs[next(iter(
        all_docs.keys()))][0].metadata)
    
    print(all_docs[next(iter(all_docs.keys()))][0:2])