import functools
from flask import Flask, render_template, blueprints, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
import sqlite3
from db import get_db

main = blueprints.Blueprint('main', __name__)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'usuario' not in session:
            return redirect(url_for('main.login'))
        return view(**kwargs)
    return wrapped_view


@main.route('/')
def index():

    return render_template("index.html")


@main.route('/BuscarAdministrador')
@login_required
def BuscarAdministrador():

    return render_template("BuscarAdministrador.html")


@main.route('/BuscarCliente')
@login_required
def BuscarCliente():

    return render_template("BuscarCliente.html")


@main.route('/ListaDeAdministradores')
@login_required
def ListaDeAdministradores():

    return render_template("ListaDeAdministradores.html")


@main.route('/listaDeClientes')
@login_required
def listaDeClientes():

    return render_template("listaDeClientes.html")


@main.route('/ListaDeHabitaciones')
@login_required
def ListaDeHabitaciones():

    return render_template("ListaDeHabitaciones.html")


@main.route('/micuenta')
@login_required
@ login_required
def micuenta():

    return render_template("micuenta.html")


@main.route('/mydata')
@login_required
def mydata():

    return render_template("mydata.html")


@main.route('/NuevaHabitacion')
@login_required
def NuevaHabitacion():

    return render_template("NuevaHabitacion.html")


@main.route('/NuevoAdministrador')
@login_required
def NuevoAdministrador():

    return render_template("NuevoAdministrador.html")


@main.route('/terminosYcondiciones')
def terminos():

    return render_template("politicasdeprivacidad.html")


@main.route('/recuperar')
def recuperarContraseña():

    return render_template("recuperarcontraseña.html")


@main.route('/reserva')
@login_required
def reserva():

    return render_template("reservas.html")

@main.route('/search')
@login_required
def search():

    return render_template("search.html")


@main.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usuario = escape(request.form['usuario'])
        contraseña = escape(request.form['password'])


        db = get_db()
        user = db.execute('select * from usuario where usuario = ? ', (usuario,)).fetchone()
        db.commit()
        db.close()
        # python -m pydoc -b

        if user is not None:
            contraseña = contraseña + usuario
            sw = check_password_hash(user[5], contraseña)

            if(sw):

                session['nombre'] = user[1]
                session['usuario'] = user[3]

                return render_template("index.html")

            flash('Usuario o clave incorrecta')

    return render_template("login.html")


@main.route('/registro', methods=['GET', 'POST'])
def registro():

    if request.method == 'POST':

        nombre = escape(request.form['nombre'])
        apellido = escape(request.form['apellido'])
        usuario = escape(request.form['usuario'])
        correo = escape(request.form['correo'])
        contraseña = escape(request.form['password'])
        telefono = escape(request.form['telefono'])

        db = get_db()
        # agregarle SLAT
        contraseña = contraseña + usuario
        contraseña = generate_password_hash(contraseña)
        db.execute("insert into usuario ( nombre, apellido, usuario, correo, contraseña, telefono) values ( ?, ?, ?, ?, ?, ?)",(nombre, apellido, usuario, correo, contraseña, telefono))
        db.commit()
        db.close()
    return render_template("registro.html")


@main.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")

