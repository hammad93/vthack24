from fastapi import FastAPI
from . import llm
app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/report")
def report(data):
    '''
    Generates the email report based on the data
    '''
    return 0

@app.get("/chat")
def api_chat(q):
    return llm.chat(query)