FROM tuxisma/flaskalpine:python3.6.4
ADD . /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apk add --update curl && \
        rm -rf /var/cache/apk/*
RUN chmod +x createsql.py \
    && python createsql.py \
    && chmod 766 crud.sqlite
CMD ["python", "crud.py"]
