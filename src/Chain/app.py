from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.Chain.inference_pipeline import Inference
import uvicorn

app = FastAPI()

class SubmitQueryRequest(BaseModel):
    query: str
    
@app.get('/')
def index():
    return 'Hello World!'
    

@app.post('/chat')
def chat(request: SubmitQueryRequest)->dict:
    try:
        prediction = Inference()
        output, ids = prediction.get_output(request.query)
        return {'response': str(output),
                'Sources': ids}
    except Exception as e:
        print(f'Error Occured {e}')
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    port = 8000
    print('Running the FastAPI server on port :', port)
    uvicorn.run("app:app", host='127.0.0.1', port = port)