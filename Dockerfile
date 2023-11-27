FROM python:3.11
WORKDIR /
COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN apt-get update && apt-get install -y build-essential libssl-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
EXPOSE 5432
