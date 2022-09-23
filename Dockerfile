FROM python:3.6.9

WORKDIR /app

RUN mkdir /app/env

# Set up virtual environment

RUN python3 -m venv /env/emotion
RUN /bin/bash -c "source /env/emotion/bin/activate"

# Install dependencies:
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD /api /app/api

ADD /ml /app/ml

ADD /checkpoints /app/checkpoints 

EXPOSE 5005

# Run the application:
CMD ["python3", "ml/src/main.py"]





