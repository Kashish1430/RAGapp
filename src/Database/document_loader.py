from langchain_community.document_loaders import PyPDFLoader
from src.utils import get_files_path

files = get_files_path('Books')

doc_loader = PyPDFLoader(files[0])
doc = doc_loader.load()

print(doc[0].page_content)
print('Source: ',doc[0].metadata['source'])
print('Page: ',doc[0].metadata['page'])

print('Combined Source: ', str(doc[0].metadata['source']) + str(doc[0].metadata['page']))
print('Number of Pages: ', len(doc))