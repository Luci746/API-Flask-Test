FROM python:3.13
WORKDIR /app
COPY . .
RUN echo "Runing image on Docker..."

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]