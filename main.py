from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from web3 import Web3
import json

# loading artifact and details
with open('build/contracts/Cert.json', 'r') as f:
    artifact = json.load(f)

with open('details.json', 'r') as f:
    details = json.load(f)

# fastapi config
app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")
templates = Jinja2Templates(directory="templates")

# web3 config
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
contract_instance = w3.eth.contract(
    address=details['contract'], abi=artifact['abi'])
print(
    f"\x1b[34mUPDATE\x1b[0m:   Instance created for Contract: {details['contract']}")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/issue")
async def get_issue(request: Request):
    return templates.TemplateResponse("issue.html", {"request": request, "message": "is-hidden"})


@app.post("/issue")
async def post_issue(request: Request, id: Annotated[str, Form()], document: Annotated[UploadFile, File()]):
    print(id)
    print(document)
    return templates.TemplateResponse("issue.html", {"request": request, "form": "is-hidden", "issued_id": id})
