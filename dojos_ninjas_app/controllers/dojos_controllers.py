from dojos_ninjas_app import app
from dojos_ninjas_app.models.dojo_model import Dojo
from flask import render_template, redirect, request


# RUTAS DE LECTURA
@app.route('/')
def raiz():
    return redirect("/dojos")

@app.route('/dojos')
def todos_los_dojos():
    todos_dojos = Dojo.mostrar_dojos()
    return render_template('dojos.html', todos_dojos = todos_dojos)

#RUTAS DE CREACION
@app.route('/creardojo', methods=['POST'])
def creardojo():
    data = {"name":request.form['dojo_name']}
    Dojo.crear_un_dojo(data)
    return redirect('/dojos')


@app.route('/dojos/<int:dojo_id>')
def mostrar_el_dojo(dojo_id):
    data = {"id":dojo_id}
    dojo = Dojo.obtener_un_dojo(data)
    ninjas_de_un_dojo = Dojo.mostrar_ninjas_del_dojo(data)
    return render_template('show.html', dojo=dojo, ninjas_de_un_dojo = ninjas_de_un_dojo)