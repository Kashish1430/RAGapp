import os
from dotenv import load_dotenv
from langchain_openai.embeddings import OpenAIEmbeddings
import glob
from pinecone import Pinecone
import re

load_dotenv()

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

def get_pinecone_api_key():
    return os.getenv("PINECONE_API_KEY")

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
