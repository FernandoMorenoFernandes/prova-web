from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

lista = []


@app.route('/', methods=['GET', 'POST'])
def index():
    total = 0
    if request.method == 'GET':
        for item in lista:
            if item['isreceita'] == 1:
                total += int(item['preco'])
            else:
                total -= int(item['preco'])
    return render_template("tela_produtos.html", itens=lista, total=total)


@app.route("/produto/novo")
def get_produto_novo():
    id = int(request.args.get("id"))
    item = {}
    if id > 0:
        item = lista[id-1]
    return render_template("produto_novo.html", item=item)


@app.route("/produto/novo", methods=["POST"])
def produto_novo():
    form_data = request.form
    index = int(request.args.get("id"))
    isreceita = int(request.args.get("receita"))
    if index > 0:
        atualizado = {
            "id": index,
            "nome": form_data["nome"],
            "preco": form_data["preco"],
            "isreceita": isreceita
        }
        lista[index-1] = atualizado
    else:
        novo = {
            "id": len(lista) + 1,
            "nome": form_data["nome"],
            "preco": form_data["preco"],
            "isreceita": isreceita
        }
        lista.append(novo)
        print(lista)

    return redirect(url_for("index"))


@app.route("/produto/excluir")
def produto_excluir():
    id = int(request.args.get("id"))
    lista.remove(lista[id-1])
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run("localhost", 55000, True)
