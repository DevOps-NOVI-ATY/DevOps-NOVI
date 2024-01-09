# Gebruik basis image van Python3
FROM python:3

#Maak een folder aan
RUN mkdir /api

# stel werk folder in van de container.
WORKDIR /api

COPY requirements.txt .

# Installeer python pakketten
RUN pip install -r requirements.txt

# Kopieer deze folder naar Workdir ( COPY . . == COPY THIS DIRECTORY TO WORKDIR)
COPY . .


