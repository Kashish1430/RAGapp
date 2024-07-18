from pinecone import Pinecone
from src.utils import connect_to_vector_database_pinecone
from src.Database.generate_embeddings import GenerateEmbeddings

class Retrival():
    def __init__(self):
        self.embedd = GenerateEmbeddings()
        self.pc = connect_to_vector_database_pinecone()
        self.Index = self.pc.Index('books-rag-app')
        
    def retrive(self, query):
        input_embedding = self.embedd.create(query)
        top_2 = self.Index.query(
            vector= input_embedding,
            top_k = 2,
            include_metadata=True)
        return top_2
    
    def clean_output(self, query):
        output = self.retrive(query)
        ids = []
        raws = []
        for match in output.matches:
            ids.append(match.id)
            raws.append(match.metadata['Raw'])
        return ids, raws

if __name__ == '__main__':
    retrive = Retrival()
    ids, raws = retrive.clean_output('What are the best practices while creating functions')
    for i, raw in enumerate(raws):
        print('----------------')
        print(ids[i])
        print(raws[i])
        
    