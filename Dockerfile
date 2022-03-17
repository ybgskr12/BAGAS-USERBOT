# Using Python Slim-Buster
FROM kyyex/kyy-userbot:busterv2
# BAGAS-USERBOT
# BAGAS

RUN git clone -b BAGAS-USERBOT https://github.com/ybgskr12/BAGAS-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ybgskr12/BAGAS-USERBOT/BAGAS-USERBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
