FROM ubuntu:16.04
RUN apt-get -y update && apt-get -y install git python3 make curl

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash
ENV NVM_DIR=/root/.nvm
SHELL ["/bin/bash"]
RUN [ -s "/root/.nvm/nvm.sh" ] && . "/root/.nvm/nvm.sh"
RUN nvm install node

COPY getPath.py /usr/bin/pyretc
RUN chmod a+x /usr/bin/pyretc

RUN git clone https://github.com/brownplt/pyret-lang.git

ENV PYRET_HOME=/pyret-lang
WORKDIR $PYRET_HOME

RUN npm install
RUN make
RUN make test

CMD /usr/bin/pyretc