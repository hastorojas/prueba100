from flask import Flask
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World !!!"

if __name__ == "__main__":
    app.run()
