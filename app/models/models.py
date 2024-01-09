import sqlalchemy as sa
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

#basis klasse voor het aanmaken van een tabel
Base = declarative_base()


stripboek_karakter = Table(
    'stripboek_karakter', Base.metadata,
    sa.Column('stripboek_naam', sa.String, ForeignKey('stripboek.naam')),
    sa.Column('stripboek_issueNummer', sa.Integer, ForeignKey('stripboek.issueNummer')),
    sa.Column('karakter_naam', sa.String, ForeignKey('karakter.naam'))
    
    # Add both columns to form a unique foreign key reference
    sa.PrimaryKeyConstraint('stripboek_naam', 'stripboek_issueNummer', 'karakter_naam')
)

stripboek_coverSoort = Table(
    'stripboek_coverSoort', Base.metadata,
    sa.Column('stripboek_naam', sa.String, ForeignKey('stripboek.naam')),
    sa.Column('stripboek_issueNummer', sa.Integer, ForeignKey('stripboek.issueNummer')),
    sa.Column('coverSoort_naam', sa.String, ForeignKey('coverSoort.naam'))
    
    # Add both columns to form a unique foreign key reference
    sa.PrimaryKeyConstraint('stripboek_naam', 'stripboek_issueNummer', 'karakter_naam')
)

stripboek_serie = Table(
    'stripboek_serie', Base.metadata,
    sa.Column('stripboek_naam', sa.String, ForeignKey('stripboek.naam')),
    sa.Column('stripboek_issueNummer', sa.Integer, ForeignKey('stripboek.issueNummer')),
    sa.Column('serie_naam', sa.String, ForeignKey('serie.naam'))
    
    # Add both columns to form a unique foreign key reference
    sa.PrimaryKeyConstraint('stripboek_naam', 'stripboek_issueNummer', 'karakter_naam')
)
class stripboek(Base):
    __tablename__ = "stripboek"

    naam = sa.Column(sa.String, primary_key=True, nullable=False)
    issueNummer = sa.Column(sa.Integer, primary_key=True, nullable=False)
    Uitgavedatum = sa.Column(sa.Date, nullable=False)
    paginas = sa.Column(sa.Integer)
    prijs = sa.Column(sa.Float)

    # Establish many-to-many relationship with karakter, coverSoort en serie
    karakters = relationship('karakter', secondary=stripboek_karakter, back_populates='stripboek')
    coverSoorten = relationship('coverSoort', secondary=stripboek_coverSoort, back_populates='stripboek')
    series = relationship('Serie', secondary=stripboek_serie, back_populates='stripboeken')

class karakter(Base):
    __tablename__ = "karakter"

    naam = sa.Column(sa.String, primary_key=True, nullable=False)

    # Establish many-to-many relationship with stripboek
    stripboeken = relationship('stripboek', secondary=stripboek_karakter, back_populates='karakters')

# Define the coverSoort class
class coverSoort(Base):
    __tablename__ = "coverSoort"

    naam = sa.Column(sa.String, primary_key=True, nullable=False)

    # Establish many-to-many relationship with stripboek
    stripboeken = relationship('stripboek', secondary=stripboek_coverSoort, back_populates='coverSoorten')

# Define the serie class
class serie(Base):
    __tablename__ = "serie"

    naam = sa.Column(sa.String, primary_key=True, nullable=False)
    serieGrootte = sa.Column(sa.Integer)
    
    # Establish one-to-many relationship with Uitgever
    uitgever = relationship('Uitgever', back_populates='series')

    # Establish many-to-many relationship with stripboek
    stripboeken = relationship('stripboek', secondary=stripboek_serie, back_populates='series')

# Define the uitgever class
class uitgever(Base):
    __tablename__ = "uitgever"

    naam = sa.Column(sa.String, primary_key=True, nullable=False)
    
    # Establish one-to-many relationship with Serie
    series = relationship('Serie', back_populates='uitgever')
    
