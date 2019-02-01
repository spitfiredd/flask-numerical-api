from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
from flask_cors import CORS

db = SQLAlchemy()
guard = Praetorian()
cors = CORS()
