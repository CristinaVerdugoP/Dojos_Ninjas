from dojos_ninjas_app import app
from dojos_ninjas_app.models.ninja_model import Ninja
from dojos_ninjas_app.models.dojo_model import Dojo
from flask import render_template, redirect, request


@app.route("/ninjas")
def formulario_ninja():
    todos_dojos = Dojo.mostrar_dojos()
    return render_template('ninjas.html', todos_dojos = todos_dojos)


@app.route("/crearninja", methods=['POST'])
def crear_ninja():
    #print(request.form, "**************")
    id_ninja = Ninja.crearninja(request.form)
    data = {"id": id_ninja}
    un_ninja = Ninja.mostrar_un_ninja(data)
    #print(un_ninja , "****************")
    return redirect(f'/dojos/{un_ninja.dojo_id}')