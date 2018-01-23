import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
<<<<<<< HEAD
    return 'Hello Ismael Garcia! I have been seen {} times.\n'.format(count)
=======
    return 'Hello Ismael! I have been seen {} times.\n'.format(count)
>>>>>>> ad785900a0f858c4f882f22e5ca61741cf65c6df

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

