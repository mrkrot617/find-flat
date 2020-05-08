from urllib import request


def send_message(ads_list, this_town):
    for item in ads_list:
        url = f"https://api.telegram.org/{BOT_ID}/" \
              f"sendMessage?chat_id={TOWNS[this_town][2]}&text=" \
              f"https://re.kufar.by/vi/{item['ad_id']}"
        try:
            request.urlopen(url)
        except:
            print('some exception: ' + this_town)