import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import random

app = Flask(__name__)

AREA_FINANZAS = 'FINANZAS'
AREA_ATENCIONALCLIENTE = 'ATENCION AL CLIENTE'

ESTADO_EN_ESPERA = 'EN ESPERA'
ESTADO_EN_PROGRESO = 'EN PROGRESO'
ESTADO_FINALIZADO = 'FINALIZADO'


ticket_list = []


@app.route("/", methods=['GET', 'POST'])
def index():
    print("metodo: " + request.method)
    if (request.method == 'GET'):
        return render_template("/tickets/ticket_new.html")
    elif (request.method == 'POST'):
        nuevo_ticket = {
            'id': random.randrange(0, 1000),
            'fecha': datetime.datetime.now(),
            'nombre': request.form["nombre"],
            'apellido': request.form["apellido"],
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
        # return "Gracias por su ticket, su numero es: " + str(nuevo_ticket["id"])


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


@app.route("/admin/")
def admin():
    return render_template("/admin/index.html")
