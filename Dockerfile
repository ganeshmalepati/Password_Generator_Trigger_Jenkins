FROM python

WORKDIR /app

COPY . /app

CMD [ "python", "Password_Generator.py" ]

