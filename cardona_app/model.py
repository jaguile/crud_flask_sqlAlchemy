from . import db_manager as db

class Llibre(db.Model):
    __tablename__ = 'llibres'

    # amb sqlite això ja és autoincremental
    id = db.Column(db.Integer, primary_key=True)
    titol = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, default='Anònim')
    prestat = db.Column(db.Integer, default=0)

class Usuari(db.Model):
    __tablename__ = 'usuaris'

    # amb sqlite això ja és autoincremental
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String, unique=True)
    nom = db.Column(db.String, nullable=False)
    cognoms = db.Column(db.String, nullable=False)
    actiu = db.Column(db.Integer, nullable=False, default=1)
