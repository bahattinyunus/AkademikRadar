# Use official Python runtime
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY core_requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r core_requirements.txt

# Copy source code
COPY . .

# Environment variables
ENV PYTHONUNBUFFERED=1

# Run the radar
ENTRYPOINT ["python", "ignite_radar.py"]
CMD ["--full"]
