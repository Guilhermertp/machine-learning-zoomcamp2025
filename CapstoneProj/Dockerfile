# -----------------------------
# 1. Base image (Python 3.13)
# -----------------------------
FROM python:3.13-slim

# -----------------------------
# 2. Environment settings
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------
# 3. Install system dependencies
# LightGBM needs gcc, g++, cmake, libgomp
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgomp1 \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# 4. Set working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# 5. Upgrade pip
# -----------------------------
RUN pip install --no-cache-dir --upgrade pip

# -----------------------------
# 6. Copy dependency file first
# -----------------------------
COPY requirements.txt .

# -----------------------------
# 7. Install Python dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# 8. Copy application code
# -----------------------------
COPY . .

# -----------------------------
# 9. Expose Flask port
# -----------------------------
EXPOSE 9696

# -----------------------------
# 10. Run the Flask app
# -----------------------------
CMD ["python", "app.py"]
