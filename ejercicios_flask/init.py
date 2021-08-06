from flask import Flask, Request
from flask.globals import request
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

post = []

@app.route('/')
def index():
    render_template("index",num_post=len(post))

@app.route('/hola',methods=['POST','GET','PUT','PATCH','DELETE'])
def hola():
    return f"Hola desde el metodo {request.method}"

@app.route('/p/<string:slug>/')
def show_post(slug):
    return render_template("post_view.html",slug_title=slug)

@app.route('/admin/post/')
@app.route('/admin/post/<int:post_id>/')
def post_form(post_id=None):
    return render_template("admin/post_form.html",post_id=post_id)

if __name__ == "__main__":
    app.run()
