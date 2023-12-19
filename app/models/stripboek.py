from models import Base
import sqlalchemy as sa

class stripboek(Base):
    __tablename__ = "stripboek"
    naam = sa.Column(sa.String, primary_key=True, nullable=False)
    issueNummer = sa.Column(sa.Integer, primary_key=True, nullable=False)
