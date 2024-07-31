import os
from dotenv import load_dotenv
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from typing import List
import glob
from pinecone import Pinecone
import re

load_dotenv()

def get_openai_api_key():
    return str(os.getenv("OPENAI_API_KEY"))

def get_pinecone_api_key():
    return str(os.getenv("PINECONE_API_KEY"))

def get_files_path(folder):
    return glob.glob(f'{folder}/*.pdf')

def get_embedding_model():
    embeddings = OpenAIEmbeddings()
    return embeddings

def generate_embeddings(blob):
    return

def connect_to_vector_database_pinecone():
    return Pinecone(api_key = get_pinecone_api_key())

def create_valid_vector_id(input_string):
    # Remove non-ASCII characters and convert to lowercase
    ascii_string = re.sub(r'[^\x00-\x7F]+', '', input_string.lower())
    
    # Replace spaces and invalid characters with dashes
    valid_id = re.sub(r'[^a-z0-9-]+', '-', ascii_string)
    
    # Remove leading/trailing dashes and ensure it's not empty
    valid_id = valid_id.strip('-') or 'default-id'
    
    return valid_id

def get_prompt_template_plain():
    template = """
    Answer the question based on the context below. If you can't 
    answer the question, reply "I don't know".

    Context: {context}

    Question: {question}
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

def get_prompt_template(context_fn: List[str], question_fn):
    template = """
    Answer the question based on the context below. If you can't 
    answer the question, reply "I don't know".

    Context: {context}

    Question: {question}
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    return prompt.format(context = get_string(context_fn), question = question_fn)

def get_string(obj):
    return ' '.join(obj)

def inspect(state):
    """Print the state passed between Runnables in a langchain and pass it on"""
    print(state)
    return state

def escape_braces(text: List[str]) -> List[str]:
    return [re.sub(r'([{}])', r'\1\1', item) for item in text]
