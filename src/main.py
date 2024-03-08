from flask import Flask, render_template, request, Query
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB("caminhos.json")

@app.route("/novo", methods=["GET","POST"])
def novo_caminho(x=None,y=None,z=None):

    Path = Query()
    add_points = True

    if request.method == "POST":
            while add_points:
                x = request.form.get("x")
                y = request.form.get("y")
                z = request.form.get("z")
                point = [x,y,z]
            db.insert({"path": {"id":1 "points":point}})

    caminhos = db.all()
    return caminhos


@app.route("/pegar_caminho", methods=["GET"])
def pegar_caminho(id):
    db.search(Path.id == id)
    

@app.route("/lista_caminhos")
def listar_caminhos():
    posts = db.all()
    for paths in posts:
        print(paths)

@app.route("/atualizar")
def atualizar_caminho(new_point, id):
    db.update({"points":new_point}, Path.id = id )

@app.route("/deletar")
def deletar_caminho(id):
    db.remove(Path.id = id)
    pass
