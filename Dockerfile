FROM dongsxyz/python-supervisord
WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py
COPY _supervisor.d/demo.conf /app/_supervisor.d/demo.conf

RUN cd /app
RUN pip install -r requirements.txt
