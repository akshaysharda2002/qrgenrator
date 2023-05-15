# Specify the base image
FROM python:3

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Set the environment variables
ENV PORT=5000
ENV NODE_ENV=production

# Expose the port the application listens on
EXPOSE $PORT

# Start the application
CMD ["python", "app.py"]
