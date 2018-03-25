FROM kennethreitz/pipenv

COPY . /app

EXPOSE 5000

RUN apt-get update
RUN apt-get install sqlite3 libsqlite3-dev
RUN sqlite3 salaries.db
RUN apt-get install build-essential

ENTRYPOINT ["python3"]

CMD ["py.api.employee/py.api.employee.py"]
