# Start from an official, lightweight Python image
FROM python:3.13-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy just the requirements file first (not all your code yet)
COPY requirements.txt .

# Install dependencies inside the container
RUN pip install -r requirements.txt

# Now copy the rest of your project files
COPY . .

# Tell Docker which port Streamlit runs on
EXPOSE 8501

# The command that runs when the container starts
CMD ["streamlit", "run", "dashboard.py", "--server.address=0.0.0.0"]