from modelo.cancion import Cancion
from modelo.interprete import Interprete
from modelo.album import Album, Medio
from modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
  session = Session()
  cancion2 = session.query(Cancion).get(2)
  session.delete(cancion2)
  session.commit()
  session.close()