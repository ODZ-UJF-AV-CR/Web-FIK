# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory
WORKDIR .

# Copy requirements.txt to the working directory
COPY requirements.txt ./

# Install app dependencies
RUN pip install fastapi[all] uvicorn
RUN pip install requests sondehub

# Bundle app source
COPY CDP.py .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your app
CMD ["uvicorn", "CDP:app","--host","0.0.0.0","--port","8000"]
