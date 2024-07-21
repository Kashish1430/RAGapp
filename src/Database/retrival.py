from pinecone import Pinecone
from src.utils import connect_to_vector_database_pinecone
from src.Database.generate_embeddings import GenerateEmbeddings

class Retrival():
    def __init__(self, top_k = 2):
        self.embedd = GenerateEmbeddings()
        self.pc = connect_to_vector_database_pinecone()
        self.Index = self.pc.Index('books-rag-app')
        self.top_n = top_k
        
    def retrive(self, query):
        input_embedding = self.embedd.create(query)
        top_2 = self.Index.query(
            vector= input_embedding,
            top_k = self.top_n,
            include_metadata=True)
        return top_2
    
    def clean_output(self, query):
        output = self.retrive(query)
        ids = []
        texts = []
        for match in output.matches:
            ids.append(match.id)
            texts.append(match.metadata.get('text', ''))
        return ids, texts

if __name__ == '__main__':
    retrive = Retrival()
    ids, raws = retrive.clean_output('What are the best practices while creating functions')
    print(raws)
    #for i, raw in enumerate(raws):
    #    print('----------------')
    #    print(ids[i])
     #   print(raws[i])