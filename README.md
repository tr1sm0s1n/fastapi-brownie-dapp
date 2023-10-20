# FastAPI-Brownie-DApp

Ethereum Certificate DApp made for Pythonistas.

## 🛠 Built With

[![Python](https://img.shields.io/badge/python-B0C4DE?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-B0C4DE?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Vyper](https://img.shields.io/badge/vyper-2F4F4F?style=for-the-badge&logo=ethereum)](https://docs.vyperlang.org/en/stable/)
[![Brownie](https://img.shields.io/badge/brownie-2F4F4F?style=for-the-badge&logo=ethereum)](https://eth-brownie.readthedocs.io/en/stable/)
[![Bulma](https://img.shields.io/badge/bulma-008080?style=for-the-badge&logo=bulma)](https://bulma.io/)

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
