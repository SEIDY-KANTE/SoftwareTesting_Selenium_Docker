FROM python:3.12

# Install PostgreSQL dependencies
RUN apt-get update && \
    apt-get install -y postgresql-client libpq-dev && \
    rm -rf /var/lib/apt/lists/*

    
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY . .


ENTRYPOINT ["sh","entrypoint.sh"]