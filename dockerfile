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

# Install Postman CLI
RUN curl -o- "https://dl-cli.pstmn.io/install/linux64.sh" | sh

# Set environment variable for Postman API key
# ARG instruction to declare a build argument
ARG POSTMAN_API_KEY_ARG

# Use the build argument in your Dockerfile as needed
ENV POSTMAN_API_KEY=$POSTMAN_API_KEY_ARG

# Run Postman login
RUN postman login --with-api-key $POSTMAN_API_KEY

# FastAPI runnen op een uvicorn server

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]

