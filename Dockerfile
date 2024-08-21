    
# Use the official Python image from the Docker Hub    
FROM python:3.9-slim    
    
# Set the working directory    
WORKDIR /app    
    
# Copy the requirements file into the Docker image    
COPY requirements.txt requirements.txt    
    
# Install the dependencies    
RUN pip install -r requirements.txt    
    
# Copy the rest of the code into the Docker image    
COPY . .    
    
# Run the application    
CMD ["python", "main.py"]    
