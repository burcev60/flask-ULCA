from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bs4 import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ulca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class Basic_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    students_count = db.Column(db.Integer)
    employee_count = db.Column(db.Integer)
    staff_count = db.Column(db.Integer)
    days_count = db.Column(db.Integer)
    otchet = db.relationship('Otchet', back_populates="basic_data")

    def __repr__(self):
        return '<Basic_data %r>' % self.id


class Energy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    energy_name = db.Column(db.String(200))
    energy_count = db.Column(db.Integer)
    energy_power = db.Column(db.Float)
    energy_time = db.Column(db.Float)
    otchet = db.relationship('Otchet', back_populates="energy")

    def __repr__(self):
        return '<Energy %r>' % self.id


class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    water_name = db.Column(db.String(200))
    water_count = db.Column(db.Integer)
    water_hot = db.Column(db.Float)
    water_cold = db.Column(db.Float)
    otchet = db.relationship('Otchet', back_populates="water")

    def __repr__(self):
        return '<Water %r>' % self.id


class Trash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trash_name = db.Column(db.String(200))
    trash_count = db.Column(db.Float)
    trash_type = db.Column(db.String(50))
    trash_style = db.Column(db.String(3))
    otchet = db.relationship('Otchet', back_populates="trash")

    def __repr__(self):
        return '<Trash %r>' % self.id


class Heat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heat_name = db.Column(db.String(200))
    delta_heat = db.Column(db.Integer)
    heat_days = db.Column(db.Integer)
    heat_square = db.Column(db.Float)
    heat_power = db.Column(db.Float)
    otchet = db.relationship('Otchet', back_populates="heat")

    def __repr__(self):
        return '<Heat %r>' % self.id

class Otchet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basic_id = db.Column(db.Integer, db.ForeignKey('basic_data.id'))
    basic_data = db.relationship('Basic_data', back_populates="otchet")
    energy_id = db.Column(db.Integer, db.ForeignKey('energy.id'))
    energy = db.relationship('Energy', back_populates="otchet")
    water_id = db.Column(db.Integer, db.ForeignKey('water.id'))
    water = db.relationship('Water', back_populates="otchet")
    trash_id = db.Column(db.Integer, db.ForeignKey('trash.id'))
    trash = db.relationship('Trash', back_populates="otchet")
    heat_id = db.Column(db.Integer, db.ForeignKey('heat.id'))
    heat = db.relationship('Heat', back_populates="otchet")
    grade_energy = db.Column(db.Float)
    grade_water = db.Column(db.Float)
    grade_trash = db.Column(db.Float)
    grade_heat = db.Column(db.Float)

    def __repr__(self):
        return '<Otchet %r>' % self.id