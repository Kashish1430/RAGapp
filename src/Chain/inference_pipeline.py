from src.Database.retrival import Retrival
from langchain_openai.chat_models import ChatOpenAI
from src.utils import get_prompt_template, get_prompt_template_plain, get_string, inspect
from src.Chain.testing_model import Model
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings


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
        self.pc = PineconeVectorStore(index_name='books-rag-app', embedding = OpenAIEmbeddings())
        
    def get_chain(self):
        if self.template is None:
            raise ValueError('Template is not set, please make sure it is set')
        return ({"context": self.pc.as_retriever(),
                 "question": RunnablePassthrough()}
                | RunnableLambda(inspect)
                | self.template | self.model.get_chain())
        #setup = self.get_runnable(self.fetched_from_pinecone)
        #return setup | self.template | self.model.get_chain()
    
    def get_output(self, query: str):
        ids, self.fetched_from_pinecone  = self.retriever.clean_output(query)
        #self.fetched_from_pinecone = get_string(fetched_from_pinecone)
        #self.template = get_prompt_template(self.fetched_from_pinecone, query)
        self.template = get_prompt_template_plain()
        print(self.template)
        chain = self.get_chain()
        return chain.invoke(query)

if __name__ == '__main__':
    prediction = Inference()
    output = prediction.get_output('What are the best practices while creating classes in python ')
    print('---------------------------------------------------------------------------------------')
    print(output)