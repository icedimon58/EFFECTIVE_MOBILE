# FROM ubuntu:22.04
FROM python
# RUN apt-get update

# RUN apt-get install -y python3.10
#
# RUN apt-get install -y pip
# RUN apt-get install -y git

RUN git clone "https://github.com/icedimon58/EFFECTIVE_MOBILE" /usr/test
# RUN pip install --upgrade

# COPY . /usr/test
RUN ls -l /usr/test
RUN pip install -r /usr/test/requirements.txt
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
# CMD ["echo","!!!!!"]
CMD ["pytest","/usr/test/tests/test_effective_mobile_main_page.py"]
# CMD ["pytest","tests/test_effective_mobile_main_page.py","--alluredir=allure-results"] && ls -l && echo  'Готово !!!'