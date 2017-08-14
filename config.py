import os

# db
DATABASE_HOST = 'localhost:3306'
DATABASE_USERNAME = 'flask'
DATABASE_PASSWORD = 'flask17admin'
DEFAULT_DATABASE = 'flaskdb'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}".format(DATABASE_USERNAME,
                                                                   DATABASE_PASSWORD,
                                                                   DATABASE_HOST,
                                                                   DEFAULT_DATABASE)

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

TEMPLATES_AUTO_RELOAD = True

# flask
#SECRET_KEY = os.environ['SECRET_KEY']
