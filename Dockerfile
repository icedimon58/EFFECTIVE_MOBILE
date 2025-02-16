
FROM python
ENV IS_DOCKER=True
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip\
        && pip install --no-cache-dir -r /app/requirements.txt\
        && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -\
        &&sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
 RUN apt-get update && apt-get install -y google-chrome-stable\
        && apt-get clean


#
# FROM python:3.10-slim
# ENV IS_DOCKER=True
# # Установим зависимости и Google Chrome
# RUN apt-get update -q && \
#     apt-get install -y --no-install-recommends wget gnupg && \
#     wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#     echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
#     apt-get update -q && \
#     apt-get install -y --no-install-recommends google-chrome-stable && \
#     apt-get clean && rm -rf /var/lib/apt/lists/ /tmp/ /var/tmp/*
# # Копируем приложение и устанавливаем зависимости
# COPY . /app
# WORKDIR /app
# RUN pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # Указываем команду по умолчанию для выполнения при запуске контейнера
CMD  ["pytest","--alluredir=allure-results"]