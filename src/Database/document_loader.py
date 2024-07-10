from langchain_community.document_loaders import PyPDFLoader
from src.utils import get_files_path

class DocumentLoader():
    def __init__(self):
        self.books = get_files_path('Books')
        
    def __len__(self):
        return len(self.books)
    
    def load_doc(self, doc):
        return PyPDFLoader(doc).load()
    
    def load_all_docs(self, books):
        document_dict = {}
        for i in range(len(books)):
            loader = PyPDFLoader(books[i])
            document_dict[books[i]] = loader.load()
        return document_dict

if __name__ == '__main__':
    doc_loader = DocumentLoader()
    print(doc_loader.books)
    print(len(doc_loader))
    #print(doc_loader.load_doc(doc_loader.books[0]))
    
    all_docs = doc_loader.load_all_docs(doc_loader.books)
    print(all_docs.keys())
    print(len(all_docs[next(iter(all_docs.keys()))]))
    print(all_docs[next(iter(
        all_docs.keys()))][0].page_content)
    print(all_docs[next(iter(
        all_docs.keys()))][0].metadata['page'])