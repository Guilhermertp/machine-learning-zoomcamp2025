# -----------------------------
# 1. Base image (Python 3.13)
# -----------------------------
FROM python:3.13-slim

# Avoid Python writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------
# 2. Install system dependencies
# LightGBM requires libgomp + gcc
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# 3. Working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# 4. Install pipenv
# -----------------------------
RUN pip install --no-cache-dir pipenv

# -----------------------------
# 5. Copy Pipenv files first
# -----------------------------
COPY Pipfile Pipfile.lock /app/

# -----------------------------
# 6. Install dependencies system-wide
# -----------------------------
RUN pipenv install --system --deploy

# -----------------------------
# 7. Copy project files
# -----------------------------
COPY . /app

# -----------------------------
# 8. Expose Flask port
# -----------------------------
EXPOSE 9696

# -----------------------------
# 9. Run the Flask API (predict.py)
# -----------------------------
CMD ["python", "predict.py"]
