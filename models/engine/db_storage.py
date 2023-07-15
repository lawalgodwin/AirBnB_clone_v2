#!/usr/bin/python3
"""DB storage engine module"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
supported_classes = {
                'User': User,
                'Review': Review,
                'Amenity': Amenity,
                'Place': Place,
                'City': City,
                'State': State
                }


class DBStorage:
    """The db storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Storage class constructor"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        dbname = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        dialet = 'mysql'
        driver = 'mysqldb'
        DB_URL = f'{dialet}+{driver}://{user}:{passwd}@{host}/{dbname}'
        self.__engine = create_engine(DB_URL, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database and tables"""
        objects = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            if cls in supported_classes.values():
                rows = self.__session.query(cls)
                for row in rows:
                    key = f'{row.__class__.__name__}.{row.id}'
                    objects.update({key: row})
        else:
            print("No class given")
            for c in supported_classes.values():
                rows = self.__session.query(c)
                for row in rows:
                    key = f"{row.__class__.__name__}.{row.id}"
                    objects[key] = row
        return objects

    def new(self, obj):
        """add the obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the new database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if obj != None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configure db and tables and reload all objects from the database"""
        Base.metadata.create_all(self.__engine)
        # create db current db session from db engine
        sessionObj = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # make sure the session is thread safe
        safeSession = scoped_session(sessionObj)
        self.__session = safeSession()
