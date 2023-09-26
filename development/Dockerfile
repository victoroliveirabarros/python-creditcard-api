FROM python:3.10

ADD development/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY development/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh \
    && ln -s /usr/local/bin/entrypoint.sh /

EXPOSE 8085

ENTRYPOINT [ "entrypoint.sh" ]
