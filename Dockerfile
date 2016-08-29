FROM fedora
RUN dnf -y install git python make curl node npm
RUN git clone https://github.com/brownplt/pyret-lang.git

RUN npm install

COPY getPath.py /usr/bin/pyretc
RUN chmod a+x /usr/bin/pyretc

ENV PYRET_HOME=/pyret-lang
WORKDIR $PYRET_HOME