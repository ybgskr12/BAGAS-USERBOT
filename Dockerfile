FROM ramadhani892/ram-ubot:slim-buster
RUN git clone -b BAGAS-USERBOT https://github.com/ybgskr12/BAGAS-USERBOT /home/bagas-userbotbot/ \
    && chmod 777 /home/bagas-userbot \
    && mkdir /home/bagas-userbot/bin/

WORKDIR /home/bagas-userbot/

CMD ["python3", "-m", "userbot"]
