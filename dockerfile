FROM debian
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3-venv \
      libgl1-mesa-glx \
      libglib2.0-0 \
      libsm6 \
      libxrender1 \
      libxext6 && \
    rm -rf /var/lib/apt/lists/*
COPY app.py requirements.txt ./
RUN python3 -m venv .venv
RUN . .venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt
CMD [".venv/bin/python", "app.py"]

