
FROM python:3.6-onbuild"
RUN apt-get update
RUN mkdir /app
RUN mkdir /openshift-client-python
COPY packages /openshift-client-python/packages
RUN mkdir /openshift-client-python
RUN pip install -r requirements.txt
ENV PYTHONPATH=/openshift-client-python/packages
ENV PYTHONUNBUFFERED=1
EXPOSE 8080
ENTRYPOINT /bin/sh
#ENTRYPOINT [ "python" ]
CMD [ "python", "app.py" ]
