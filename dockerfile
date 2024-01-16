# Gebruik basis image van Python3
FROM python:3.10.13-slim

#Maak een folder aan
RUN mkdir /api

# stel werk folder in van de container.
WORKDIR /api

COPY requirements.txt .

# Installeer python pakketten
RUN pip install -r requirements.txt

# Kopieer deze folder naar Workdir ( COPY . . == COPY THIS DIRECTORY TO WORKDIR)
COPY . .

# Expose the necessary ports
EXPOSE 8000
EXPOSE 5432

# FastAPI runnen op een uvicorn server
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
