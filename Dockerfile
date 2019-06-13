FROM python:2.7
ADD ./getMacInfo.py /
ADD ./README /
RUN pip install requests
#CMD [ "python", "./getMacInfo.py"]
ENTRYPOINT ["./getMacInfo.py"]
