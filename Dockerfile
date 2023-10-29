# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY deal /app/deal
COPY deal_codegen.py /app/deal_codegen.py
COPY proto /app/proto
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# -r requirements.txt

ENV SERVER_IP 0.0.0.0
ENV SERVER_PORT 50053

# Expose the port the service will run on
EXPOSE 50053

# Run the gRPC service when the container launches
WORKDIR /app

# Define environment variable
RUN set -x && \
    python deal_codegen.py

WORKDIR /app/deal

CMD ["python", "deal.py"]
