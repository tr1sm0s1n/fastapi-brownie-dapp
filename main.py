from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from web3 import Web3
import json


class Certificate(BaseModel):
    id: int
    name: str
    course: str
    grade: str
    date: str
    document: bytes


with open('details.json', 'r') as f:
    details = json.load(f)

with open('build/contracts/Cert.json', 'r') as f:
    artifact = json.load(f)

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")
templates = Jinja2Templates(directory="templates")

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
contract_instance = w3.eth.contract(
    address=details['contract'], abi=artifact['abi'])
print(
    f"\x1b[34mUPDATE\x1b[0m:   Instance created for Contract: {details['contract']}")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Certificate DApp"})


@app.get("/issue")
async def issue(request: Request):
    return templates.TemplateResponse("issue.html", {"request": request, "title": "Certificate DApp"})
