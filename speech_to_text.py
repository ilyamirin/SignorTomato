#!python3
import urllib.request
import json
import os

FOLDER_ID = "b1gs8d8gurpgig5h56km" # Идентификатор каталога
IAM_TOKEN = os.getenv('IAM_TOKEN') # IAM-токен


def stt(filename):
    with open(filename, "rb") as f:
        data = f.read()

    params = "&".join([
        "topic=general",
        "folderId=%s" % FOLDER_ID,
        "lang=ru-RU"
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)
    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    if decodedData.get("error_code") is None:
        print(decodedData.get("result"))

    os.remove(filename)


while True:
    for filename in os.listdir('./'):
        if filename.endswith(".ogg"):
            stt(filename)
        continue
    else:
        continue
