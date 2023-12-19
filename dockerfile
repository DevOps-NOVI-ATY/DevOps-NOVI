# Gebruik basis image van Python3
FROM python:3

#Maak een folder aan
RUN mkdir /app

# stel werk folder in van de container.
WORKDIR /app

COPY requirements.txt .

# Installeer python pakketten
RUN pip install -r requirements.txt

# Kopieer deze folder naar Workdir ( COPY . . == COPY THIS DIRECTORY TO WORKDIR)
COPY . .

# FastAPI runnen op een uvicorn server
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]