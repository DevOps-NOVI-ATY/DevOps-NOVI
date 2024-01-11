from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship

#basis klasse voor het aanmaken van een tabel
Base = declarative_base()


Serie_strip = Table(
    'serie_strip',
    Base.metadata,
    sa.Column('serie', ForeignKey('serie.naam'), primary_key=True),
    sa.Column('stripboek', ForeignKey('stripboek.naam'), primary_key=True),    
)

Strip_kar = Table(
    'strip_kar',
    Base.metadata,
    sa.Column('stripboek', ForeignKey('stripboek.naam'), primary_key=True),
    sa.Column('karakter', ForeignKey('karakter.naam'), primary_key=True),    
)

Strip_cover = Table(
    'strip_cover',
    Base.metadata,
    sa.Column('stripboek', ForeignKey('stripboek.naam'), primary_key=True),
    sa.Column('cover_soort', ForeignKey('cover_soort.naam'), primary_key=True),    
)


# Define the uitgever class
class Uitgever(Base):
    __tablename__ = "uitgever"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    series = relationship("Serie", back_populates="uitgever")

      
class Serie(Base):
    __tablename__ = "serie"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    serieGrootte = sa.Column(sa.Integer)
    uitgever_naam = sa.Column(sa.String, ForeignKey("uitgever.naam"))
    uitgever = relationship("Uitgever", back_populates="series")
    stripboeken = relationship('Stripboek', secondary='serie_strip', back_populates='series')


class Stripboek(Base):
    __tablename__ = "stripboek"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    issueNummer = sa.Column(sa.Integer, nullable=False)
    Uitgavedatum = sa.Column(sa.Date, nullable=False)
    paginas = sa.Column(sa.Integer)
    prijs = sa.Column(sa.Float)
    series = relationship('Serie', secondary='serie_strip', back_populates='stripboeken')
    karakters = relationship('Karakter', secondary='strip_kar', back_populates='stripboeken')
    covers = relationship('Cover_soort', secondary='strip_cover', back_populates='stripboeken')



class Karakter(Base):
    __tablename__ = "karakter"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    stripboeken = relationship('Stripboek', secondary='strip_kar', back_populates='karakters')


class Cover_soort(Base):
    __tablename__ = "cover_soort"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    stripboeken = relationship('Stripboek', secondary='strip_cover', back_populates='covers')


