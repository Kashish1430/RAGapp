from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.Chain.inference_pipeline import Inference
import uvicorn
import os

print("OPENAI_API_KEY:", os.environ.get("OPENAI_API_KEY", "Not set")[:5] + "..." if os.environ.get("OPENAI_API_KEY") else "Not set")
print("PINECONE_API_KEY:", os.environ.get("PINECONE_API_KEY", "Not set")[:5] + "..." if os.environ.get("PINECONE_API_KEY") else "Not set")

curr_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(curr_dir, '..', '..'))

static_dir = os.path.join(project_root, 'static')
template_dir = os.path.join(project_root, 'template')

app = FastAPI()
app.mount('/static', StaticFiles(directory=static_dir), name='static')

templates = Jinja2Templates(directory=template_dir)

class SubmitQueryRequest(BaseModel):
    query: str
    
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request':request})
    

@app.post('/chat')
def chat(request: SubmitQueryRequest)->dict:
    try:
        prediction = Inference()
        output, ids = prediction.get_output(request.query)
        return {'response': str(output),
                'sources': ids}
    except Exception as e:
        print(f'Error Occured {e}')
        raise HTTPException(status_code=500, detail=str(e))

#app = uvicorn.run(app, host='0.0.0.0', port=8000)
if __name__ == '__main__':
    port = 8000
    uvicorn.run("app:app", host='0.0.0.0', port = port, reload=True)
    