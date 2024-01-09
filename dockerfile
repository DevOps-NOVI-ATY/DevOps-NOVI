# Stage 1: Build stage
FROM python:3 AS builder

#Maak een folder aan
RUN mkdir /api

# Create a folder for the application
WORKDIR /api

COPY requirements.txt .

# Install Python packages
RUN pip install -r requirements.txt

# Copy the entire application to the working directory
COPY . .

# Stage 2: Postman stage
FROM builder AS postman

# Install Postman CLI
RUN curl -o- "https://dl-cli.pstmn.io/install/linux64.sh" | sh

# Set environment variable for Postman API key
ARG POSTMAN_API_KEY_ARG

# Use the build argument in your Dockerfile as needed
ENV POSTMAN_API_KEY=$POSTMAN_API_KEY_ARG

# Run Postman login
RUN postman login --with-api-apikey $POSTMAN_API_KEY

# Stage 3: Final stage
FROM python:3

# Set the working directory inside the container
WORKDIR /api

# Copy only necessary files from the postman stage
COPY --from=postman /usr/local/bin/postman /usr/local/bin/postman
COPY --from=postman /root/.config/configstore/pman.json /root/.config/configstore/pman.json

# Copy the application files
COPY --from=builder /api .

# FastAPI runnen op een uvicorn server
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
