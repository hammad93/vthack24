from fastapi import FastAPI
from . import llm
from . import main_mail
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
    Based on the above data about a user's location and weather data from the National Weather Service,
    please generate a HTML email report which includes information about any alerts.
    '''
    result = llm.chat(query)
    return result['choices'][0]['message']['content']

@app.get("/email")
def send_mail(body, recipient):
    return main_mail.send_email(body, recipient)

@app.get("/chat")
def api_chat(q):
    return llm.chat(q)