from fastapi import FastAPI
from . import llm
from . import main_mail
from . import images
app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/send_report")
def send_report(data, recipient):
    query = f'''{data}
    From the above data about weather please generate a HTML email report. Provide nothing but the HTML code.
    '''
    result = llm.chat(query)
    report = result['choices'][0]['message']['content'].replace('\n', '').replace('```', '')
    img_url = images.generate(f"A nature portrait describing {q}")
    imag_tag = f'<img src="{img_url}"><br/>'
    main_mail.send_email(image_tag + report, recipient)

@app.get("/report")
def report(data):
    '''
    Generates the email report based on the data
    '''
    query = f'''{data}
    From the above data about weather please generate a HTML email report. Provide nothing but the HTML code.
    '''
    result = llm.chat(query)
    return result['choices'][0]['message']['content'].replace('\n', '').replace('```', '')

@app.get("/email")
def send_mail(body, recipient):
    return main_mail.send_email(body, recipient)

@app.get("/chat")
def api_chat(q):
    return llm.chat(q)

@app.get("/image")
def image(q):
    return images.generate(f"A nature portrait describing {q}")