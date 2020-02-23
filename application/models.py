from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    fave_rec=db.relationship('Favourites', backref='favourite_recipes', lazy=True)

    def __repr__(self):
       	return '' .join([
             'UserID: ', str(self.id), '\r\n',
             'Email: ', self.email, '\r\n',
             'Name: ', self.first_name, ' ', self.last_name
        ])

    @login_manager.user_loader
    def load_user(id):
    	return Users.query.get(int(id))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False, unique=True)
    image = db.Column(db.String(1000), nullable=False, unique=True)
    ingredients = db.Column(db.String(1000), nullable=False, unique=True)
    method = db.Column(db.String(1000), nullable=False, unique=True)
    fave_rec=db.relationship('Favourites', backref='recipe', lazy=True)

    def __repr__(self):
        return ''.join([
            'Name: ', self.name, '\r\n', 'Ingredients', self.ingredients
            ])

class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    name = db.Column(db.String(1000), nullable=False, unique=True)
    image = db.Column(db.String(1000), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Name: ', self.name, '\r\n', 'Ingredients', self.ingredients
            ])
