# Use the official Python base image
FROM python:3

RUN mkdir /app
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory ( COPY . . == COPY THIS DIRECTORY TO WORKDIR)
COPY . .

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]