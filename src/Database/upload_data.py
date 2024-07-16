from pinecone import Pinecone
from src.utils import connect_to_vector_database_pinecone
from src.Database.document_loader import DocumentLoader
from src.Database.generate_embeddings import GenerateEmbeddings


class UploadData():
    def __init__(self):
        self.pc = connect_to_vector_database_pinecone()
        self.doc_loader = DocumentLoader()
        self.gen_embed = GenerateEmbeddings()
        self.Index = self.pc.Index('books-rag-app')
        
    def upload_docs(self):
        all_docs = self.gen_embed.load_obj('embeddings.pkl')
        print('Generating Embeddings Done')
        for doc_name, pages in all_docs.items():
            print('New Doc')
            i =0 
            for page in pages:
                i += 1
                try:
                    
                    print('Uploading Data to pinecone')
                    print(i)
                    self.Index.upsert(
                        vectors = [{
                        "id":page.metadata,
                        "values":page.embedding,
                        "metadata": {'Raw': page.page_content}
                        }])
                except:
                    pass
        print('Upload Finished')

if __name__ == '__main__':
    upload = UploadData()
    upload.upload_docs()