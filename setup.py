
RUN yum --enablerepo=extras install -y epel-release && \
    yum install -y git python3 python-pip && \
    pip install paramiko pyyaml prometheus_client boto3 slackclient && \
    mkdir /openshift-client-python

COPY packages /openshift-client-python/packages

ENV PYTHONPATH=/openshift-client-python/packages
ENV PYTHONUNBUFFERED=1

ENTRYPOINT /bin/sh
