FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc libgl1 libglib2.0-0 dos2unix \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Convert ALL files to Linux format (fix CRLF issue)
RUN find . -type f -exec dos2unix {} \;

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

#IMPORTANT: run uvicorn directly (no shell)
ENTRYPOINT ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]