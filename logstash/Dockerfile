ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN apk --update add openjdk8-jre \
                     curl

RUN curl https://artifacts.elastic.co/downloads/logstash/logstash-6.0.0.tar.gz \
        --output /tmp/logstash-6.0.0.tar.gz
RUN tar xvzf /tmp/logstash-6.0.0.tar.gz -C /usr/bin/
RUN rm /tmp/logstash-6.0.0.tar.gz


CMD [ "/usr/bin/run.sh" ]