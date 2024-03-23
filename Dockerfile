FROM python:3.11-alpine

# Install necessary system packages
RUN apk add --no-cache \
    build-base \
    lapack-dev \
    gfortran \
    musl-dev \
    libffi-dev

ENV HOST=0.0.0.0
 
ENV LISTEN_PORT 8080
 
EXPOSE 8080

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["streamlit", "run", "Application.py", "--server.port=8080", "--server.address=0.0.0.0"]
