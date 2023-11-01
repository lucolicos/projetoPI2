from flask import Flask, render_template

app = Flask(__name__)


'#colocar o site no ar'
'#route -> rota do link'
'#função -. o que você quer exibir naquela página'
'#template'


@app.route("/")
def homepage():
    return render_template("HomepagePI2.html")


@app.route("/telapedidos")
def telapedidos():
    return render_template("TeladepedidosPI2.html")


@app.route("/usuarios/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuarios.html",nome_usuario=nome_usuario)


'#colocar o site no ar'
if __name__ == "__main__":
    app.run(debug=True)
