FROM python:3

ENV COUNTRYAPP 1

RUN mkdir /countryapp
WORKDIR /countryapp
ADD requirements.txt /countryapp/
RUN pip install -r requirements.txt
ADD . /countryapp/

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]