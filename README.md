# FastAPI-Brownie-DApp

Ethereum Certificate DApp made for Pythonistas.

## 🛠 Built With

<div align="left">
<a href="https://docs.python.org/3/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/python.svg" width="36" height="36" alt="Python" /></a>
<a href="https://eth-brownie.readthedocs.io/en/stable/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/ethereum.svg" width="36" height="36" alt="Ethereum" /></a>
<a href="https://docs.vyperlang.org/en/stable/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/vyper.svg" width="36" height="36" alt="Vyper" /></a>
<a href="https://fastapi.tiangolo.com/tutorial/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/fastapi.svg" width="36" height="36" alt="FastAPI" /></a>
<a href="https://bulma.io/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/bulma.svg" width="36" height="36" alt="Bulma" /></a>
</div>

## ⚙️ Run Locally

Clone the repository

```bash
git clone https://github.com/DEMYSTIF/fastapi-brownie-dapp.git
cd fastapi-brownie-dapp
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the environment

> For Linux

```bash
source /venv/bin/activate
```

> For Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

Workaround for PyYAML

```bash
echo 'Cython < 3.0' > /tmp/constraint.txt
PIP_CONSTRAINT=/tmp/constraint.txt pip wheel PyYAML==5.4.1
```

Install packages

```bash
pip install -r requirements.txt
```

Compile the contract

```bash
brownie compile
```

Test the contract

```bash
brownie test
```

Run a blockchain (ganache/geth/foundry) on port **8545**.

Deploy the contract

```bash
brownie run deploy_cert.py
```

Start the application

```bash
uvicorn main:app --reload
```

## 📜 License

Click [here](./LICENSE.md).

## 🎗️ Contributing

Click [here](./CONTRIBUTING.md).

## ⚖️ Code of Conduct

Click [here](./CODE_OF_CONDUCT.md).
