ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk --update add python3
# RUN pip install request

COPY ./src /usr/bin

CMD [ "/usr/bin/backupconfig.py" ]