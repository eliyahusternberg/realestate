# realestate
import os
basedir=os.path.abspath(os.path.dirname(__file__))
#print("basedir: ", basedir )

class Config(object):   
    SECRET_KEY =os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'app.db')
    LANGUAGES = ['en','he','es']
    #print("SQLALCHEMY_DATABASE_URI: ", SQLALCHEMY_DATABASE_URI )

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME ='eliyahusternberg@gmail.com'
    MAIL_PASSWORD = 'Btalyz12!'
    ADMINS = ['eliyahusternberg@gmail.com']
    SQLALCHEMY_TRACK_MODIFICATIONS=False        
    POSTS_PER_PAGE = 25
