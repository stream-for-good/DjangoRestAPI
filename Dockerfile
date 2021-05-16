from python:3
COPY requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt
RUN mkdir -p /opt/s4g/
COPY * /opt/s4g/
WORKDIR /opt/s4g
ENTRYPOINT ["python3","./manage.py","runserver","0.0.0.0:8000"]
