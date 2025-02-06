# FROM ubuntu:22.04
FROM python
# RUN apt-get update

# RUN apt-get install -y python3.10
#
# RUN apt-get install -y pip
# RUN apt-get install -y git

RUN git clone "https://github.com/icedimon58/EFFECTIVE_MOBILE" ./usr/test
# RUN pip install --upgrade

# COPY . /usr/test
RUN pip install -r /usr/test/requirements.txt


CMD ls -l && cd /usr/test && ls -l && pwd && echo 'Готово !!!'