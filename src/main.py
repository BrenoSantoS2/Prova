#Primeiro de tudo, não consegui entender muito de flask então minha solução não roda por tanto, acho que tera que ser feita uma analise apenas da lógica do código, ou pode zerar tudo que vou entender.

from flask import Flask, render_template, request, Query
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB("caminhos.json")

@app.route("/novo", methods=["GET","POST"])
def novo_caminho(x=None,y=None,z=None):

    Path = Query()
    add_points = True

    #Tentei fazer um algoritimo que requisitasse cada eixo de um ponto para que o usuário respondesse e assim formasse um ponto, para que posteriormente o ponto fosse adicionado a um dicionário chamado Path, que iria possuir um id e os pontos ligados a ele.

    #Além do mais tentei colocar um while para que ele pudesse ir criando vários pontos dentro desse dicionário Path, entretanto não consegui concluir a lógica pois tenho muitas dúvidas sobre o Flask principalmente

    #Além do mais tive dificuldades em desenvolver a lógica do Id, pois não sei como o código pode conferir os ids que já existem e aplicar apenas novos ids para os novos caminhos.

    if request.method == "POST":
            while add_points:
                x = request.form.get("x")
                y = request.form.get("y")
                z = request.form.get("z")
                point = [x,y,z]
            db.insert({"path": {"id":1 "points":point}})

    caminhos = db.all()
    return caminhos

# Aqui é uma o usuário pode encontrar o caminho que quer pelo ID
@app.route("/pegar_caminho", methods=["GET"])
def pegar_caminho(id):
   return db.search(Path.id == id)
    
# Aqui o usuário recebe uma lista de todos os caminhos
@app.route("/lista_caminhos")
def listar_caminhos():
    lista_de_caminhos = []
    posts = db.all()
    for paths in posts:
        listar_caminhos.append(paths)

# Aqui o usuário consegue atualizar os pontos de um caminho por ID
@app.route("/atualizar")
def atualizar_caminho(new_point, id):
    db.update({"points":new_point}, Path.id = id )

# Aqui o usuário pode deletar um caminho pelo seu ID
@app.route("/deletar")
def deletar_caminho(id):
    db.remove(Path.id = id)
    pass
