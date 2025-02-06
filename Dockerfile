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
RUN pip install -r /usr/test/requirments.txt
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
# CMD ["pytest", "tests/test_main.py", "--alluredir=allure-results"]
CMD ls -l && cd /usr/test && ls -l && pwd &&  ["pytest", "tests/test_main.py", "--alluredir=allure-results"] && ls -l && echo  'Готово !!!'