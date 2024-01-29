from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship



#Base class
base = declarative_base()


series_comics = Table(
    'series_comics',
    base.metadata,
    sa.Column('series', ForeignKey('series.name'), primary_key=True),
    sa.Column('comics', ForeignKey('comics.name'), primary_key=True),    
)

comics_char = Table(
    'comics_char',
    base.metadata,
    sa.Column('comics', ForeignKey('comics.name'), primary_key=True),
    sa.Column('characters', ForeignKey('characters.name'), primary_key=True),    
)

comics_covers = Table(
    'comics_covers',
    base.metadata,
    sa.Column('comics', ForeignKey('comics.name'), primary_key=True),
    sa.Column('covers', ForeignKey('covers.type'), primary_key=True),    
)


# Define the uitgever class
class publishers(base):
    __tablename__ = "publishers"

    name = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    series = relationship("series", back_populates="publishers")

      
class series(base):
    __tablename__ = "series"

    name = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    size = sa.Column(sa.Integer)
    publisher = sa.Column(sa.String, ForeignKey("publishers.name"))
    publishers = relationship("publishers", back_populates="series")
    comics = relationship('comics', secondary='series_comics', back_populates='series')


class comics(base):
    __tablename__ = "comics"

    name = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    issue = sa.Column(sa.Integer, nullable=False)
    release = sa.Column(sa.Date, nullable=False)
    pages = sa.Column(sa.Integer)
    price = sa.Column(sa.Float)
    series = relationship('series', secondary='series_comics', back_populates='comics')
    characters = relationship('characters', secondary='comics_char', back_populates='comics')
    covers = relationship('covers', secondary='comics_covers', back_populates='comics')



class characters(base):
    __tablename__ = "characters"

    name = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    comics = relationship('comics', secondary='comics_char', back_populates='characters')


class covers(base):
    __tablename__ = "covers"

    type = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    comics = relationship('comics', secondary='comics_covers', back_populates='covers')


