ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk --update add python3
# RUN pip install request

RUN mkdir /opt
COPY ./src /opt

CMD [ "/opt/backupconfig.py" ]