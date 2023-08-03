FROM mcr.microsoft.com/playwright:focal

WORKDIR /
COPY . /
RUN apt-get update
RUN yes | apt-get install python3-pip
RUN pip install -r requirements.txt
RUN pip install python-dotenv
RUN pip install playwright
RUN pip install requests
RUN playwright install
RUN playwright install chrome
RUN apt install unzip
RUN wget https://github.com/allure-framework/allure2/releases/download/2.15.0/allure-2.15.0.zip && unzip allure-2.15.0.zip
RUN apt-get -y install openjdk-11-jdk
RUN pip install allure-pytest
RUN pip install pytest-rerunfailures
RUN pip install pytest-playwright

ENTRYPOINT ["bash","entrypoint.sh"]