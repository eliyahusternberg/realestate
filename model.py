# realestate
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
from time import time
import jwt
from app import app


class User(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), index=True,unique=True)
    email =db.Column(db.String(120),index=True, unique=True)
    password_hash = db.Column(db.String(128))


class Buyer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(64),index=True)
    Phone_number=db.Column(db.Integer(12))
    Address = db.Column(db.String(60))
    Email =db.Column(db.String(120),index=True,unique=True)
    Company =db.Column(db.String(30),index=True)
    Job = db.Column(db.String(30)index=True)
    Title = db.Column(db.String(30)index=True)
    Refered_by=db.Column(db.String(30)index=True)
    Contact_info=db.Column(db.String(25)index=True)
    Nickname = db.Column(db.String(25)index=True)
    Website =db.Column(db.String(50)index=True,unique=True)
    Reffered = db.Column(db.String(30)index=True)
    Intent=db.Column(db.String(20))
    Notes = Column(db.String(1000))
   
class BuildingProfile(db.model):
     State = db.Column(db.String(25))
     City = db.Column(db.String(20))
     County = db.Column(db.String(25))
     County =db.Column(db.Ss = "dddtring(20))
     Type = db.Column(db.String(30))
     Price_buillding_area =db.Column(db.Integer)
     Stories = db.Column(db.Integer)
     Units=db.Column(db.Interger)
     Tax = db.Column(db.Integer)
     Sale_date=db.Column(db.Integer)
     Sale_amount = db.Column(db.Integer)
     minimum_sale_amount
     maximum_sale_amount
     Price_per_building_area = db.Column(db.Integer)
     Price_per_unit = db.Column(db.Integer)
     Price_per_square_foot = db.Column(db.Integer)
     Far = db.Column(db.Integer)
     Irr = db.Column(db.Integer)
     cap = db.Column(db.Integer)
     Operating_income =db.Column(db.Integer)
     Gross_income = db.Column(db.Integer)
     Operating_cost = db.Column(db.Integer)
     Debt =db.Column(db.Integer)
     Equity = db.Column(db.Integer)
     Comission = db.Column(db.Integer)
     Owners_details = db.Column(db.String(100))
     Financing = db.Column(db.Integer)

class Property(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(64),index=True)
    Phone_number=db.Column(db.Integer(12))
    Address = db.Column(db.String(60))
    Email =db.Column(db.String(120),index=True,unique=True)
    Company =db.Column(db.String(30),index=True)
    Job = db.Column(db.String(30)index=True)
    Title = db.Column(db.String(30)index=True)
    Refered_by=db.Column(db.String(30)index=True)
    Contact_info=db.Column(db.String(25)index=True)
    Nickname = db.Column(db.String(25)index=True)
    Website =db.Column(db.String(50)index=True,unique=True)
    Reffered = db.Column(db.String(30)index=True)
    Intent=db.Column(db.String(20))
    Notes = Column(db.String(1000))
    State = db.Column(db.String(25))
    City = db.Column(db.String(20))
    County = db.Column(db.String(25))
    Country = db.Column(db.String(20))
    Type = db.Column(db.String(30))
    Price_buillding_area =db.Column(db.Integer)
    Stories = db.Column(db.Integer)
    Units = db.Column(db.Integer)
    Tax = db.Column(db.Integer)
    Sale_date=db.Column(db.Integer)
    Sale_amount = db.Column(db.Integer)
    Price_per_building_area = db.Column(db.Integer)
    Price_per_unit = db.Column(db.Integer)
    Price_per_square_foot = db.Column(db.Integer)
    Far = db.Column(db.Integer)
    Irr = db.Column(db.Integer)
    cap = db.Column(db.Integer)
    Operating_income =db.Column(db.Integer)
    Gross_income = db.Column(db.Integer)
    Operating_cost = db.Column(db.Integer)
    Debt =db.Column(db.Integer)
    Equity = db.Column(db.Integer)
    Comission = db.Column(db.Integer)
    Owners_details = db.Column(db.String(100))
    Financing = db.Column(db.IInteger)

      
