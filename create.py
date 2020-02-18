from application import db
from application.models import Posts, Users
import csv

db.drop_all()
db.create_all()
