from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from src.utils import get_openai_api_key

class Model():
    def __init__(self, model_type='gpt-3.5-turbo'):
        super().__init__()
        self.model = ChatOpenAI(openai_api_key=get_openai_api_key(), model='gpt-3.5-turbo')
        self.parser = StrOutputParser()

    def get_chain(self):
        return self.model | self.parser
    
    def predict(self, query):
        chain = self.get_chain()
        return chain.invoke(query)
    
template = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
prompt.format(context = "My name is Kashish Rajput and i am from india, i am known as the best swimmer of my country", 
              question = "Who is the best swimmer in india? ")

#chain = prompt | model | parser

#output = chain.invoke({'context': "My name is Kashish Rajput and i am from india, i am known as the best swimmer of my country", 
#              'question' : "Who is the best swimmer in india? "})

#print(output)

if __name__ == '__main__':
    model = Model()
    outputs = model.predict('Who is the Best dancer in india?')
    print(outputs)