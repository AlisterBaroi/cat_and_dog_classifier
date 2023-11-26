FROM python:3.11.6-slim

ENV HOST=0.0.0.0
 
ENV LISTEN_PORT 8080
 
EXPOSE 8080

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port", "8080"]