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
    name = db.Column(db.String(64),index=True)
    phone_number=db.Column(db.Integer(12))
    address = db.Column(db.String(60))
    email =db.Column(db.String(120),index=True,unique=True)
    company =db.Column(db.String(30),index=True)
    job = db.Column(db.String(30)index=True)
    title = db.Column(db.String(30)index=True)
    refered_by=db.Column(db.String(30)index=True)
    contact_info=db.Column(db.String(25)index=True)
    nickname = db.Column(db.String(25)index=True)
    website =db.Column(db.String(50)index=True,unique=True)
    reffered = db.Column(db.String(30)index=True)
    intent=db.Column(db.String(20))
    notes = Column(db.String(1000))
   
class BuildingProfile(db.model):
    state = db.Column(db.String(25))
    city = db.Column(db.String(20))
    county = db.Column(db.String(25))
    county =db.Column(db.String(20))
    category= db.Column(db.String(30))
    price_buillding_area =db.Column(db.Integer)
    stories = db.Column(db.Integer)
    units=db.Column(db.Interger)
    tax = db.Column(db.Integer)
    sale_date=db.Column(db.Integer)
    sale_amount = db.Column(db.Integer)
    minimum_sale_amount = db.comlumn(db.Interger)
    maximum_sale_amount = db.comlumn(db.Interger)
    price_per_building_area = db.Column(db.Integer)
    price_per_unit = db.Column(db.Integer)
    price_per_square_foot = db.Column(db.Integer)
    far = db.Column(db.Integer)
    irr = db.Column(db.Integer)
    cap = db.Column(db.Integer)
    operating_income =db.Column(db.Integer)
    gross_income = db.Column(db.Integer)
    operating_cost = db.Column(db.Integer)
    debt =db.Column(db.Integer)
    equity = db.Column(db.Integer)
    comission = db.Column(db.Integer)
    owners_details = db.Column(db.String(100))
    financing = db.Column(db.Integer)

class Property(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),index=True)
    phone_number=db.Column(db.Integer(12))
    address = db.Column(db.String(60))
    email =db.Column(db.String(120),index=True,unique=True)
    company =db.Column(db.String(30),index=True)
    job = db.Column(db.String(30)index=True)
    title = db.Column(db.String(30)index=True)
    refered_by=db.Column(db.String(30)index=True)
    contact_info=db.Column(db.String(25)index=True)
    nickname = db.Column(db.String(25)index=True)
    website =db.Column(db.String(50)index=True,unique=True)
    reffered = db.Column(db.String(30)index=True)
    intent=db.Column(db.String(20))
    notes = Column(db.String(1000))
    state = db.Column(db.String(25))
    city = db.Column(db.String(20))
    county = db.Column(db.String(25))
    country = db.Column(db.String(20))
    category = db.Column(db.String(30))
    price_buillding_area =db.Column(db.Integer)
    stories = db.Column(db.Integer)
    units = db.Column(db.Integer)
    tax = db.Column(db.Integer)
    sale_date=db.Column(db.Integer)
    sale_amount = db.Column(db.Integer)
    asking_price =  = db.comlumn(db.Interger)
    # not sure if this shoud be in BuyersProfile or in this class
    offering_price = = db.comlumn(db.Interger)
    price_per_building_area = db.Column(db.Integer)
    price_per_unit = db.Column(db.Integer)
    price_per_square_foot = db.Column(db.Integer)
    far = db.Column(db.Integer)
    irr = db.Column(db.Integer)
    cap = db.Column(db.Integer)
    operating_income =db.Column(db.Integer)
    gross_income = db.Column(db.Integer)
    operating_cost = db.Column(db.Integer)
    debt =db.Column(db.Integer)
    equity = db.Column(db.Integer)
    comission = db.Column(db.Integer)
    owners_details = db.Column(db.String(100))
    financing = db.Column(db.IInteger)

      
