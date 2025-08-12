from flask import Blueprint, render_template, redirect, url_for, request, current_app
from . import db_manager as db
from .model import Llibre, Usuari

# Blueprint
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/")
def mostrar_llibres():
    llibres = db.session.query(Llibre).all()
    usuaris = db.session.query(Usuari).filter(Usuari.actiu.like(1)).all()
    return render_template("cataleg.html", llibres = llibres, usuaris = usuaris)

@main_bp.route("/add", methods=['GET'])
def afegir_llibre():
    titol = request.args.get ("titol", type=str)
    autor = request.args.get ("autor", default="Anònim", type=str)

    if autor == '':
        autor = "Anònim"

    llibreAfegit = Llibre(titol = titol, autor = autor)
    
    db.session.add(llibreAfegit)
    db.session.commit()

    return redirect(url_for('main_bp.mostrar_llibres'))

@main_bp.route("/del", methods=['POST'])
def esborrar_llibres():
    llibres = request.form.getlist('llibre', type=int)
    print(llibres)
    for id in llibres:
        llibreEsborrat = db.get_or_404(Llibre, id)
        db.session.delete(llibreEsborrat)
    db.session.commit()
    return redirect(url_for('main_bp.mostrar_llibres'))

@main_bp.route("/prestec", methods=['GET'])
def prestar_llibre():
    
    idLlibre = request.args.get('idLlibre', type=int)
    idUsuari = request.args.get('idUsuari', type=int)
    
    llibrePrestat = db.get_or_404(Llibre, idLlibre)
    llibrePrestat.prestat = idUsuari
    
    db.session.commit()
    
    return redirect(url_for('main_bp.mostrar_llibres'))

@main_bp.route("/usr")
def mostrar_usuaris():
    usuaris = db.session.query(Usuari).filter(Usuari.actiu.like(1)).all()
    return render_template("usuaris.html", usuaris = usuaris)

@main_bp.route("/baixes")
def mostrar_baixes():
    usuaris = db.session.query(Usuari).filter(Usuari.actiu.like(0)).all()
    return render_template("baixes.html", usuaris = usuaris)

@main_bp.route("/afegir", methods=['POST'])
def afegir_usuari():

    dni = request.form.get ("dni", type=str)
    nom = request.form.get ("nom", type=str)
    cognoms = request.form.get ("cognoms", type=str)

    usuariNou = Usuari(dni = dni, nom = nom, cognoms = cognoms)
    
    db.session.add(usuariNou)
    db.session.commit()

    return redirect(url_for('main_bp.mostrar_usuaris'))

@main_bp.route("/baixa", methods=['POST'])
def baixa_usuaris():
    usuaris = request.form.getlist('usuari', type=int)

    for id in usuaris:
        usuariBaixa = db.get_or_404(Usuari, id)
        usuariBaixa.actiu = 0
    db.session.commit()
    return redirect(url_for('main_bp.mostrar_baixes'))

@main_bp.route("/alta", methods=['POST'])
def alta_usuaris():
    usuaris = request.form.getlist('usuari', type=int)

    for id in usuaris:
        usuariAlta = db.get_or_404(Usuari, id)
        usuariAlta.actiu = 1
    db.session.commit()
    return redirect(url_for('main_bp.mostrar_baixes'))

@main_bp.route("/prestecs")
def veure_usuari():
    idUsuari    = request.args.get('id', type=int)
    usuari      = db.get_or_404(Usuari, idUsuari)

    llibres     = db.session.execute(db.select(Llibre).where(Llibre.prestat == idUsuari)).scalars().all()

    return render_template("prestecs_usuari.html", usuari = usuari, llibres = llibres)

@main_bp.route("/join")
def mostrar_join():

    user_id = Usuari.id.label('user_id')
    
    resultJoin = db.session.execute(db.select(Llibre.id, Llibre.autor, Llibre.titol, user_id, Usuari.dni, Usuari.nom, Usuari.cognoms).select_from(Llibre).join(Usuari, Llibre.prestat == Usuari.id)).all()
    print("****************")
    print (resultJoin)
    # return render_template("join.html", llibres = resultJoin)
    return render_template("join.html", llibres = resultJoin)