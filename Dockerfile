FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install mkdocs mkdocs-material mkdocs-jupyter

EXPOSE 8000

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]