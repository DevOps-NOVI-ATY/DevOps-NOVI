FROM python:3.10-slim

ARG DATABASE_URL_ARG

ENV DATABASE_URL=$DATABASE_URL_ARG

#Maak een folder aan
WORKDIR /api

# Kopieer deze folder naar Workdir ( COPY . . == COPY THIS DIRECTORY TO WORKDIR)
COPY . .

# Installeer python pakketten
RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 5432

# Get latest alembic db version
# RUN alembic upgrade head
RUN chmod +x /api/entrypoint.sh
# FastAPI runnen op een uvicorn server
ENTRYPOINT [ "bash", "/api/entrypoint.sh" ]
