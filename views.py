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


@main.route('/NuevaHabitacion', methods=['GET', 'POST'])
@login_required
def NuevaHabitacion():
    if request.method == 'POST':

        CodHab = escape(request.form['codigoHabitacion'])
        Numpiso = escape(request.form['numPiso'])
        Precio = escape(request.form['precio'])

        db = get_db()

        db.execute("insert into habitacion ( CodHab, Numpiso, Precio ) values ( ?, ?, ?)", (CodHab, Precio, Numpiso))
        db.commit()
        db.close()
        return render_template("ListaDeHabitaciones.html")

    return render_template("NuevaHabitacion.html")


@main.route('/NuevoAdministrador', methods=['GET', 'POST'])
@login_required
def NuevoAdministrador():

    if request.method == 'POST':
        cedula = escape(request.form['cedula'])
        nombre = escape(request.form['nombreAdministrador'])
        apellido = escape(request.form['apellidoAdminsitrador'])
        telefono = escape(request.form['telefonoAdministrador'])
        direccion = escape(request.form['direccionAdministrador'])
        usuario = escape(request.form['nombreAdministrador'])
        correo = escape(request.form['emailAdministrador'])
        contrase??a = escape(request.form['passwordAdmministrador'])
        rol = escape(request.form['ROL'])
        
        db = get_db()

        db.execute("insert into administrador ( cedula, nombre, apellido, telefono, direccion, usuario, correo, contrase??a, rol) values ( ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (cedula, nombre, apellido, telefono, direccion, usuario, correo, contrase??a, rol))
        db.commit()
        db.close()
        return render_template("ListaDeAdministradores.html")

    return render_template("NuevoAdministrador.html")


@main.route('/terminosYcondiciones')
def terminos():

    return render_template("politicasdeprivacidad.html")


@main.route('/recuperar')
def recuperarContrase??a():

    return render_template("recuperarcontrase??a.html")


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
        contrase??a = escape(request.form['password'])


        db = get_db()
        user = db.execute('select * from usuario where usuario = ? ', (usuario,)).fetchone()
        superadmin = db.execute('select * from superadministrador where usuario = ? ', (usuario,)).fetchone()
        db.commit()
        db.close()
        # python -m pydoc -b

        if user is not None:
            contrase??a = contrase??a + usuario
            sw = check_password_hash(user[5], contrase??a)

            if(sw):

                session['nombre'] = user[1]
                session['usuario'] = user[3]
                session['password'] = user[5]
                session['rol'] = user[7]

                return render_template("index.html")

            flash('Usuario o clave incorrecta')

        if superadmin is not None:
            contrase??a = contrase??a + usuario
            sw = check_password_hash(superadmin[5], contrase??a)

            if(sw):

                session['nombre'] = superadmin[1]
                session['usuario'] = superadmin[3]
                session['password'] = superadmin[5]
                session['rol'] = superadmin[7]

                return render_template("micuenta.html")

            flash('Usuario o clave incorrecta')

    return render_template("login.html")


@main.route('/registro', methods=['GET', 'POST'])
def registro():

    if request.method == 'POST':

        nombre = escape(request.form['nombre'])
        apellido = escape(request.form['apellido'])
        usuario = escape(request.form['usuario'])
        correo = escape(request.form['correo'])
        contrase??a = escape(request.form['password'])
        telefono = escape(request.form['telefono'])

        db = get_db()
        # agregarle SLAT
        contrase??a = contrase??a + usuario
        contrase??a = generate_password_hash(contrase??a)
        db.execute("insert into usuario ( nombre, apellido, usuario, correo, contrase??a, telefono, rol) values ( ?, ?, ?, ?, ?, ?, ?)",(nombre, apellido, usuario, correo, contrase??a, telefono, 'user'))
        db.commit()
        db.close()
        return render_template("login.html")
    return render_template("registro.html")


@main.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")

