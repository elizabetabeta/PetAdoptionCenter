from model import *
from model.relacije import *
from model.cache import region, api

#docker exec -it redis-stack redis-cli

korisnik = User(name="Pero", lastname="Peric", email="email@email.com", 
                phone_number="123456", user_type="user")
session.add(korisnik)
session.commit()

