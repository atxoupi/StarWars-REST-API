from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(8), nullable=False)
    favoriteUser = db.relationship('favoritos', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }    

class Personajes(db.Model):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    lastname = db.Column(db.String(250))
    id_planeta = db.Column(db.Integer, ForeignKey('planetas.id'), nullable=False)
    ojos = db.Column(db.String(20))
    pelo = db.Column(db.String(20))
    altura= db.Column(db.Integer)
    peso= db.Column(db.Integer)
    favoritePersonaje = db.relationship('personajes', backref='user', lazy=True)

class Planetas(db.Model):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    clima = Column(String(250))
    poblacion = Column(Integer)
    rotacion = Column(String(20))
    planetPersonaje = relationship('personajes', backref='planetas', lazy=True)
    favoritePlanet = relationship('planetas', backref='user', lazy=True)

class Vehiculos(db.Model):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cilindrada = Column(Integer)
    capacidad = Column(Integer)
    favoriteVehiculo = relationship('favoritos', backref='vehiculos', lazy=True)
    

class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'),nullable=False)
    id_personaje = Column(Integer, ForeignKey('personajes.id'),nullable=False)
    id_planeta = Column(Integer, ForeignKey('planetas.id'),nullable=False)
    id_vehiculo = Column(Integer, ForeignKey('vehiculos.id'),nullable=False)

    def to_dict(self):
        return {}




# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }