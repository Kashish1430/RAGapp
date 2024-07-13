import os
from dotenv import load_dotenv
from langchain_openai.embeddings import OpenAIEmbeddings
import glob

load_dotenv()

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

def get_files_path(folder):
    return glob.glob(f'{folder}/*.pdf')

def get_embedding_model():
    embeddings = OpenAIEmbeddings()
    return embeddings

def generate_embeddings(blob):
    return