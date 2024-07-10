from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from src.utils import get_openai_api_key
import glob

list_files = glob.glob('Books/*.pdf')
API_KEY = get_openai_api_key()
model = ChatOpenAI(openai_api_key=API_KEY, model="gpt-3.5-turbo")
parser = StrOutputParser()

chain = model | parser
#output = chain.invoke('Hello How are you, who made you ?')
template = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
output = prompt.format(context="Good software systems begin with clean code. On the one hand, if the bricks aren’t well made, the architecture of the building doesn’t matter much. On the other hand, you can make a substantial mess with well-made bricks. This is where the SOLID principles come in. ",
              question = 'What is the good software system practice? ')


chain_2 = prompt | chain
#output = chain_2.invoke({
#    'context':"Good software systems begin with clean code. On the one hand, if the bricks aren’t well made, the architecture of the building doesn’t matter much. On the other hand, you can make a substantial mess with well-made bricks. This is where the SOLID principles come in. ",
#     'question': 'What is the good software system practice? '})

doc_loader = PyPDFLoader(list_files[0])
doc = doc_loader.load()
print(doc)