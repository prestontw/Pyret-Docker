FROM ubuntu:16.04
RUN apt-get -y update && apt-get -y install git python3 make

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash
RUN nvm install node

COPY getPath.py /usr/bin/pyretc
RUN chmod a+x /usr/bin/pyretc

RUN git clone https://github.com/brownplt/pyret-lang.git

ENV PYRET_HOME=/pyret-lang
WORKDIR $PYRET_HOME

RUN npm install
RUN make
RUN make test
