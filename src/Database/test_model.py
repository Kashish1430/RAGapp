from langchain_openai.chat_models import ChatOpenAI
from src.utils import get_openai_api_key

API_KEY = get_openai_api_key()

model = ChatOpenAI(openai_api_key=API_KEY, model="gpt-3.5-turbo")

model.invoke("Hello how are you and who made you ?")

