FROM python:3
RUN mkdir /omni_seeker
WORKDIR /omni_seeker
COPY requirements.txt /omni_seeker/
RUN pip install -r requirements.txt
COPY . /omni_seeker/