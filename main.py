import json
from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from web3 import Web3

# loading artifact and details
with open('build/contracts/Cert.json', 'r', -1, 'utf-8') as f:
    artifact = json.load(f)

with open('details.json', 'r', -1, 'utf-8') as f:
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
async def post_issue(request: Request, _id: Annotated[int, Form()], name: Annotated[str, Form()], course: Annotated[str, Form()], grade: Annotated[str, Form()], date: Annotated[str, Form()]):
    trx = contract_instance.functions.issue(
        _id, name, course, grade, date).transact({"from": details["deployer"]})
    trx_hash = trx.hex()
    trx_receipt = w3.eth.get_transaction_receipt(trx_hash)
    print(trx_receipt)
    return templates.TemplateResponse("issue.html", {"request": request, "form": "is-hidden", "issued_id": _id})


@app.post("/certificate")
async def fetch_certificate(request: Request, _id: Annotated[int, Form()]):
    result = contract_instance.functions.Certificates(_id).call()
    return templates.TemplateResponse("certificate.html", {"request": request, "_id": _id, "name": result[0], "course": result[1], "grade": result[2], "date": result[3]})
