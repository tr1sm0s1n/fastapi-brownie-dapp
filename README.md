# FastAPI-Brownie-DApp

Ethereum Certificate DApp made for Pythonistas.

## 🛠 Built With

[![Python](https://img.shields.io/badge/python-steelblue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-steelblue?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Vyper](https://img.shields.io/badge/vyper-darkslategray?style=for-the-badge&logo=ethereum&logoColor=white)](https://docs.vyperlang.org/en/stable/)
[![Brownie](https://img.shields.io/badge/brownie-darkslategray?style=for-the-badge&logo=ethereum&logoColor=white)](https://eth-brownie.readthedocs.io/en/stable/)
[![Bulma](https://img.shields.io/badge/bulma-indigo?style=for-the-badge&logo=bulma&logoColor=white)](https://bulma.io/)

## ⚙️ Run Locally

Clone the repository

```bash
git clone https://github.com/tr1sm0s1n/fastapi-brownie-dapp.git
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

Install Brownie

```bash
pip install eth-brownie
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

Install FastAPI

```bash
pip install "fastapi[all]"
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
