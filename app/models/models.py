import sqlalchemy as sa
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

#basis klasse voor het aanmaken van een tabel
Base = declarative_base()



serie_strip = Table(
    'serie_strip',
    Base.metadata,
    sa.Column('serie', ForeignKey('serie.naam'), primary_key=True),
    sa.Column('stripboek', ForeignKey('stripboek.naam'), primary_key=True),    
)

strip_kar = Table(
    'strip_kar',
    Base.metadata,
    sa.Column('stripboek', ForeignKey('stripboek.naam'), primary_key=True),
    sa.Column('karakter', ForeignKey('karakter.naam'), primary_key=True),    
)

strip_cover = Table(
    'strip_cover',
    Base.metadata,
    sa.Column('stripboek', ForeignKey('stripboek.naam'), primary_key=True),
    sa.Column('cover_soort', ForeignKey('cover_soort.naam'), primary_key=True),    
)


# Define the uitgever class
class uitgever(Base):
    __tablename__ = "uitgever"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    series = relationship("serie", back_populates="uitgever")

      
class serie(Base):
    __tablename__ = "serie"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    serieGrootte = sa.Column(sa.Integer)
    uitgever_naam = sa.Column(sa.String, ForeignKey("uitgever.naam"))
    uitgever = relationship("uitgever", back_populates="serie")
    stripboeken = relationship('stripboek', secondary='serie_strip', back_populates='serie')

class stripboek(Base):
    __tablename__ = "stripboek"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    issueNummer = sa.Column(sa.Integer, nullable=False)
    Uitgavedatum = sa.Column(sa.Date, nullable=False)
    paginas = sa.Column(sa.Integer)
    prijs = sa.Column(sa.Float)
    series = relationship('serie', secondary='serie_strip', back_populates='stripboek')
    karakters = relationship('karakter', secondary='strip_kar', back_populates='stripboek')
    covers = relationship('cover_soort', secondary='strip_cover', back_populates='stripboek')



class karakter(Base):
    __tablename__ = "karakter"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    stripboeken = relationship('stripboek', secondary='strip_kar', back_populates='karakter')


class cover_soort(Base):
    __tablename__ = "cover_soort"

    naam = sa.Column(sa.String, primary_key=True, nullable=False, unique=True)
    stripboeken = relationship('stripboek', secondary='strip_cover', back_populates='cover_soort')


