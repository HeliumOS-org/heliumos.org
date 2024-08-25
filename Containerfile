FROM quay.io/almalinuxorg/9-base

WORKDIR /workdir

RUN dnf upgrade -y

RUN dnf install -y \
    make \
    npm \
    python3.12-pip \
    python3.12-mod_wsgi

RUN python3.12 -m pip install uv

COPY . .

RUN uv venv

RUN make sync

RUN make migrate

RUN make load

RUN make build

RUN dnf install -y httpd && \
    mkdir -p /usr/local/apache2/conf/ && \
    cp -r httpd.conf /etc/httpd/conf.d/httpd.conf

EXPOSE 80
CMD httpd -DFOREGROUND
