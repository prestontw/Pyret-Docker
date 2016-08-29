FROM fedora
RUN dnf -y install git python make curl node npm
RUN git clone https://github.com/brownplt/pyret-lang.git

ENV PYRET_HOME=/pyret-lang
WORKDIR $PYRET_HOME

RUN npm install

COPY getPath.py /usr/bin/pyretc
RUN chmod a+x /usr/bin/pyretc

RUN ls build/phase0
