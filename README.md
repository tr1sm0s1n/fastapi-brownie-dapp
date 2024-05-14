# FastAPI-Brownie-DApp

Ethereum Certificate DApp made for Pythonistas.

## 🛠 Built With

[![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)](https://www.python.org/)
[![FastAPI Badge](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff&style=for-the-badge)](https://fastapi.tiangolo.com)
[![Vyper Badge](https://img.shields.io/badge/Vyper-3C3C3D?logo=ethereum&logoColor=fff&style=for-the-badge)](https://docs.vyperlang.org/en/stable/)
[![Brownie Badge](https://img.shields.io/badge/Brownie-3C3C3D?logo=ethereum&logoColor=fff&style=for-the-badge)](https://eth-brownie.readthedocs.io/en/stable/)
[![Bulma Badge](https://img.shields.io/badge/Bulma-00D1B2?logo=bulma&logoColor=fff&style=for-the-badge)](https://bulma.io/)

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
source ./venv/bin/activate
```

> For Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

Install Brownie

```bash
pip install eth-brownie
```

Compile the contract

```bash
brownie compile
```

Run a blockchain simulation (geth/hardhat/foundry) on port **8545**.

Test the contract

```bash
brownie test
```

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
