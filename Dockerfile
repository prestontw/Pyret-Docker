FROM ubuntu:16.04
RUN apt-get -y update && apt-get -y install git python3 make nodejs npm

RUN ln -s /usr/bin/nodejs /usr/bin/node

COPY getPath.py /usr/bin/pyretc

RUN git clone https://github.com/brownplt/pyret-lang.git

ENV PYRET_HOME=/pyret-lang
WORKDIR $PYRET_HOME

RUN npm install
RUN make
RUN make test
