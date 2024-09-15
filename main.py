from fastapi import FastAPI
from . import llm
from . import main_mail
from . import images
app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/report")
def report(data):
    '''
    Generates the email report based on the data
    '''
    query = f'''{data}
    From the above data about weather please generate a HTML email report. Provide nothing but the HTML code.
    '''
    result = llm.chat(query)
    return result['choices'][0]['message']['content']

@app.get("/email")
def send_mail(body, recipient):
    return main_mail.send_email(body, recipient)

@app.get("/chat")
def api_chat(q):
    return llm.chat(q)

@app.get("/image")
def image(q):
    return images.generate(f"What it looks like out a window when it's {q}")