from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ulca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Basic_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    students_count = db.Column(db.Integer)
    employee_count = db.Column(db.Integer)
    staff_count = db.Column(db.Integer)
    days_count = db.Column(db.Integer)

    def __repr__(self):
        return '<Basic_data %r>' % self.id


class Energy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    energy_name = db.Column(db.String(200))
    energy_count = db.Column(db.Integer)
    energy_power = db.Column(db.Float)
    energy_time = db.Column(db.Float)

    def __repr__(self):
        return '<Energy %r>' % self.id


class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    water_name = db.Column(db.String(200))
    water_count = db.Column(db.Integer)
    water_hot = db.Column(db.Float)
    water_cold = db.Column(db.Float)

    def __repr__(self):
        return '<Water %r>' % self.id


class Trash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trash_name = db.Column(db.String(200))
    trash_count = db.Column(db.Float)
    trash_type = db.Column(db.String(50))
    trash_style = db.Column(db.String(3))

    def __repr__(self):
        return '<Trash %r>' % self.id


class Teplo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    floor_count = db.Column(db.Integer)
    teplo_days = db.Column(db.Integer)
    teplo_name = db.Column(db.String(200))
    teplo_square = db.Column(db.Float)
    teplo_power = db.Column(db.Float)

    def __repr__(self):
        return '<Teplo %r>' % self.id