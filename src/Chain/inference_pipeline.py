from src.Database.retrival import Retrival
from langchain_openai.chat_models import ChatOpenAI
from src.utils import get_prompt_template, get_prompt_template_plain, get_string, inspect
from src.Chain.testing_model import Model
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate


class PrintContext():
    def __call__(self, context):
        print('context being provided')
        print(context)
        return context
    
class Inference():
    def __init__(self):
        self.retriever = Retrival(top_k = 2)
        self.model = Model()
        self.template = None
        self.fetched_from_pinecone = None
        self.pc = PineconeVectorStore.from_existing_index(index_name='books-rag-app', embedding = OpenAIEmbeddings())
        
    def get_chain(self):
        if self.template is None:
            raise ValueError('Template is not set, please make sure it is set')
        
        prompt = ChatPromptTemplate.from_template(self.template)
        print(self.model.get_chain())
        return prompt | self.model.get_chain()
    
    def get_output(self, query: str):
        
        #results = self.pc.similarity_search_with_score(query, k=2)
        #context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        #print(context)
        
        ids, self.fetched_from_pinecone  = self.retriever.clean_output(query)
        print('---------------------------------------------------------------------------------------')
        print(self.fetched_from_pinecone)
        self.fetched_from_pinecone = get_string(self.fetched_from_pinecone)
        self.template = get_prompt_template(self.fetched_from_pinecone, query)
        print(self.template)
        
        chain = self.get_chain()
        print(chain)
        return chain.invoke({'context': self.fetched_from_pinecone, 'question': query})

if __name__ == '__main__':
    prediction = Inference()
    output = prediction.get_output('What are the best practices while creating classes in python ')
    print('---------------------------------------------------------------------------------------')
    print(output)