FROM python:3.9

RUN pip install pipenv

ADD . /webapp

WORKDIR /webapp

RUN pipenv install --system --skip-lock

RUN rq worker tasks

EXPOSE 5000

CMD flask run
