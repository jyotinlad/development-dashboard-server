FROM python:3.7

COPY . /development-dashboard-server

WORKDIR /development-dashboard-server

RUN pip install -r python_requirements.txt

ENTRYPOINT ["python"]

CMD ["dashboard.py"]
