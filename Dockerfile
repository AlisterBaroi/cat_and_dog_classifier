FROM python:3.11-slim-bullseye

ENV HOST=0.0.0.0
 
ENV LISTEN_PORT 8080
 
EXPOSE 8080

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port", "8080"]