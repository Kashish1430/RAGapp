from src.Database.retrival import Retrival
from langchain_openai.chat_models import ChatOpenAI
from src.utils import get_prompt_template, get_prompt_template_plain, get_string, inspect, escape_braces
from src.Chain.testing_model import Model
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
import sys

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
        print('Template', self.template)
        prompt = ChatPromptTemplate.from_template(self.template)
        return prompt | self.model.get_chain()
    
    def get_output(self, query: str):
        
        #results = self.pc.similarity_search_with_score(query, k=2)
        #context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        #print(context)
        
        ids, self.fetched_from_pinecone  = self.retriever.clean_output(query)
        self.fetched_from_pinecone = escape_braces(self.fetched_from_pinecone)
        self.template = get_prompt_template(self.fetched_from_pinecone, query)
        chain = self.get_chain()
        return chain.invoke({'context': self.fetched_from_pinecone, 'question': query}), ids

if __name__ == '__main__':
    import os
    if len(sys.argv)<2:
        print('Please enter the question.')
    else:
        prediction = Inference()
        input_by_user = " ".join(sys.argv[1:])
        print('Question asked by the user: ', input_by_user)
        output, sources = prediction.get_output(input_by_user)
        print(output)
        print('\nSources of the output: ',sources)
        
        print("OPENAI_API_KEY:", os.environ.get("OPENAI_API_KEY", "Not set")[:5] + "..." if os.environ.get("OPENAI_API_KEY") else "Not set")
        print("PINECONE_API_KEY:", os.environ.get("PINECONE_API_KEY", "Not set")[:5] + "..." if os.environ.get("PINECONE_API_KEY") else "Not set")
