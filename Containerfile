FROM quay.io/almalinuxorg/9-base

WORKDIR /build

RUN dnf upgrade -y

RUN dnf install -y \
    make \
    npm \
    python3-pip

RUN python3 -m pip install uv

RUN uv python install 3.12

COPY . .

RUN uv venv

RUN make deps

RUN make sync

RUN make load

RUN make build

RUN dnf install -y httpd && \
    cp -r dist/* /var/www/html/

RUN rm -rdf /build

EXPOSE 80
CMD httpd -DFOREGROUND
