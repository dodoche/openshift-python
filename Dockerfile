
FROM centos:7

RUN yum --enablerepo=extras install -y epel-release && \
    yum install -y git python2 python-pip && \
    pip install paramiko pyyaml prometheus_client boto3 slackclient && \
    mkdir /openshift-client-python

COPY packages /openshift-client-python/packages

ENV PYTHONPATH=/openshift-client-python/packages
ENV PYTHONUNBUFFERED=1
ENV APP_ENV development

# Exposing Ports
EXPOSE 5035

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application
CMD ["python", "app.py"]

ENTRYPOINT /bin/sh


