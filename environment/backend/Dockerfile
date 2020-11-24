FROM python:3.8
ENV PYTHONBUFFERED 1

WORKDIR /backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY ./backend .
WORKDIR /backend/blog_crm
EXPOSE 8000
