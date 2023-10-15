#!/usr/bin/python
""" Holds class Amenity """
import models
from models.base_model import BaseModel
from os import getenv

if models.storage_t == "db":
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship
    from models.base_model import Base


class Amenity(BaseModel):
    """ Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

        place_amenities = relationship("Place", secondary="place_amenity")

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes Amenity """
        super().__init__(*args, **kwargs)
