from psycopg2 import connect
from time import sleep
from datetime import datetime
import ads
import db_utils
import messages


BOT_ID = 'bot1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

TOWNS = {
         'brest': ['1', '23.641487,52.021919,23.787812,52.158843', 'CHAT_ID'],
         'gomel': ['2', '30.881999,52.390761,31.051750,52.490685', 'CHAT_ID'],
         'grodno': ['3', '23.766091,53.606835,23.963845,53.726724', 'CHAT_ID'],
         'mogilev': ['4', '30.229468,53.833438,30.399001,53.970047', 'CHAT_ID'],
         'vitebsk': ['6', '30.089889,55.125103,30.306854,55.268390', 'CHAT_ID'],
         'minsk': ['7', '27.397665,53.814539,27.696236,53.980569', 'CHAT_ID']}

connection = connect(host="db", database="ads", user="user", password="password")


for town in TOWNS:
    req_url = 'https://cre-api.kufar.by/ads-search/v1/engine/v1/search/raw?' \
              f'sort=lst.d&size=30&cat=1010&typ=let&rnt=1&rgn={TOWNS[town][0]}' \
              f'&gbx=b:{TOWNS[town][1]}'

    json_response = ads.get_json_response(req_url)
    ad_list = ads.get_ads(json_response)
    unique_ads = db_utils.pg_connect(connection, ad_list, town)

    messages.send_message(unique_ads, town)
    sleep(1)
    print("done")
