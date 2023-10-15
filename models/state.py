#!/usr/bin/python3
""" Holds class State """
import models
from models.base_model import BaseModel

if models.storage_t == "db":
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship
    from models.base_model import Base
    from models.city import City


class State(BaseModel):
    """ Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes state """
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """ Getter for list of city instances related to the state """
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
