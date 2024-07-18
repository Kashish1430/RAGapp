import logging
from pinecone import Pinecone
from src.utils import connect_to_vector_database_pinecone
from src.Database.document_loader import DocumentLoader
from src.Database.generate_embeddings import GenerateEmbeddings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
            j = 0
            i =0 
            for page in pages:
                i += 1
                j += 1
                try:
                    if len(page.embedding) != 0: 
                        print('Uploading Data to pinecone')
                        logging.info(f'Uploading Data to Pinecone: {doc_name}, Page: {i}')
                        self.Index.upsert(
                            vectors = [{
                            "id":page.metadata,
                            "values":page.embedding,
                            "metadata": {'Raw': page.page_content}
                            }])
                except Exception as e:
                    logging.error(f"Error uploading {doc_name}, Page {i}: {e}")
                    logging.debug(f"Failed page data: id={page.metadata}, values={page.embedding}, metadata={'Raw': page.page_content}")
        print('Total Docs Uploaded ', j)
        print('Upload Finished')

if __name__ == '__main__':
    upload = UploadData()
    upload.upload_docs()