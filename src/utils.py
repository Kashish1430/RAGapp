import os
from dotenv import load_dotenv
import glob

load_dotenv()

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

def get_files_path(folder):
    return glob.glob(f'{folder}/*.pdf')
