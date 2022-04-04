from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="")

@app.get("/lol")
async def createElement(request: Request, header, text):

   return templates.TemplateResponse("main.html", {"request":request,"navigation":[{"header":header,"text":text}]})
