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

# FastAPI runnen op een uvicorn server
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
