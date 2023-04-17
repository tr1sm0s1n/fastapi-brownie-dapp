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
python -m venv venv
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

Install packages

```bash
pip -r requirements.txt
```

Compile the contract

```bash
brownie compile
```

Test the contract

```bash
brownie test
```

Run a blockchain (ganache/geth/foundry) on http://127.0.0.1:8545

Deploy the contract

```bash
brownie run deploy_cert.py
```

Start the application

```bash
uvicorn main:app --reload
```

## 📜 License

Distributed under the MIT License.

## 🎗️ Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/<feature_name>`)
3. Commit your Changes (`git commit -m '<feature_name>_added'`)
4. Push to the Branch (`git push origin feature/<feature_name>`)
5. Open a Pull Request
