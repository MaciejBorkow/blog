FROM python:3.8
ENV PYTHONBUFFERED 1

WORKDIR /backend
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /backend/blog_crm
