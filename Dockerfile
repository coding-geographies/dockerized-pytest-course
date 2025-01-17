FROM python:3.12

RUN mkdir /pytest_project/
COPY ./test-requirements.txt /pytest_project/
COPY ./setup.py ./setup.py

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip3 install -r /pytest_project/test-requirements.txt

WORKDIR /pytest_project/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
