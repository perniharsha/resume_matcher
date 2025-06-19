FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    && apt-get clean

# Give execution permission to the start.sh script inside the container
RUN chmod +x start.sh

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 8501

CMD ["./start.sh"]
