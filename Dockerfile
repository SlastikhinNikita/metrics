FROM python:3
MAINTAINER Nikita Slastikhin <slastikhin.nikita@gmail.com>
ADD metrics.py /
RUN pip install psutil
ENTRYPOINT ["python", "./metrics.py"]

