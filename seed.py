from models import db, Pet
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name = 'Meow', species='cat', photo_url="https://placekitten.com/200/300", age="baby",notes="3 weeks old")
pet2 = Pet(name='Bark',species='dog', photo_url="", age="adult", notes="reserved",available=False )



db.session.add(pet1)
db.session.add(pet2)
db.session.commit()