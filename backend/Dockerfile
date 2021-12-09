FROM python:3.8
ENV PYTHONBUFFERED 1
ARG UID
ARG GID
RUN groupadd -g ${GID} user && useradd -u ${UID} -g ${GID} user

WORKDIR /backend
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /backend/blog_crm
USER user
