FROM fedora:23
RUN dnf -y install python-setuptools git; easy_install pip
RUN pip install -U pip
RUN pip install Django PyYAML
RUN git clone https://github.com/psav/jvis
ADD setup.sh /setup.sh
EXPOSE 8000
ENTRYPOINT ["sh", "setup.sh"]
