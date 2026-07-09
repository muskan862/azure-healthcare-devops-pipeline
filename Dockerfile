# Step 1: Choose a base image (The OS and language runtime environment)
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy your dependency list into the container
COPY requirements.txt .

# Step 4: Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code into the container
COPY . .

# Step 6: Inform Docker which port the container listens on at runtime
EXPOSE 5000

# Step 7: Define the command to run your app when the container starts
CMD ["python", "app.py"]