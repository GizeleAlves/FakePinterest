from fakepinterest2 import database, app
from fakepinterest2.models import Usuario,Foto

with app.app_context():
    database.create_all()