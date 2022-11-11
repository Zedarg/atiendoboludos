import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import random

app = Flask(__name__)

# el orden importa!
# al ser importada desde el archivo users.py,
# esta lista tiene que existir antes de que se importe users.py
user_list = [{
    "id": 1,
    "name": "John",
    "lastname": "Doe",
    "email": "johndoe@tuvieja.com"
}]

from modules import users

AREA_FINANZAS = 'FINANZAS'
AREA_ATENCIONALCLIENTE = 'ATENCION AL CLIENTE'

ESTADO_EN_ESPERA = 'EN ESPERA'
ESTADO_EN_PROGRESO = 'EN PROGRESO'
ESTADO_FINALIZADO = 'FINALIZADO'


ticket_list = []
user_list = []

@app.get("/")
def index():
    return render_template("/tickets/ticket_new.html")

@app.post("/")
def ticket_new():
    nuevo_ticket = {
        'id': random.randrange(0, 1000),
        'fecha': datetime.datetime.now(),
        'nombre': request.form["nombre"],
        'apellido': request.form["apellido"],
        'email': request.form["email"],
        'area': request.form["area"],
        'descripcion': request.form["descripcion"],
        'estado': ESTADO_EN_ESPERA,
        'devolucion': ''
    }
    ticket_list.append(nuevo_ticket)
    return f'''
            <h1>El ticket se ha creado correctamente</h1>
            <p>Ticket Nro: {str(nuevo_ticket["id"])}</p>
            <a href="/">Volver</a>
        '''

@app.route("/admin/tickets")
def tickets():
    return render_template("/tickets/ticket_list.html", tickets=ticket_list)


@app.route("/admin/tickets/<int:id>")
def ticket_detail(id):
    # voy a la base de datos y obtengo el ticket con el id
    # ese ticket lo mando al render template
    ticket_encontrado = None
    for ticket in ticket_list:
        if ticket["id"] == id:
            ticket_encontrado = ticket
            break
    return render_template("/tickets/ticket_detail.html", ticket=ticket_encontrado)


# cerrar ticket
# @app.post("/admin/tickets/<int:id>/close")
# def ticket_close(id):
    # buscar el ticket a modificar en el listado
    # modificar el estado del ticket
    # guardar el ticket modificado
    # redirigir a la lista de tickets

@app.route("/admin/")
def admin():
    return render_template("/admin/index.html")
