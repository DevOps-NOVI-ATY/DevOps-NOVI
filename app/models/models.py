from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

#basis klasse voor het aanmaken van een tabel
Base = declarative_base()


class uitgever(Base):
    __tablename__ = "uitgever"
    naam = sa.Column(sa.String, primary_key=True, nullable=False)


class series(Base):
    __tablename__ = "series"
    naam = sa.Column(sa.String, primary_key=True, nullable=False)
    grootte = sa.Column(sa.INTEGER, nullable=False)

