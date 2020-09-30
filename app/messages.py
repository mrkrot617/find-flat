from urllib import request

def send_message(ads_list, town, bot_id, chat_id):

    for item in ads_list:

        if item['company_ad']:
            is_owner = "%D0%9D%D0%95%D0%A2"
        else:
            is_owner = "%D0%94%D0%90"

        url = f"https://api.telegram.org/{bot_id}/" \
              f"sendMessage?chat_id={chat_id}&text=" \
              f"%D0%92%D0%BB%D0%B0%D0%B4%D0%B5%D0%BB%D0%B5%D1%86%20({is_owner}):%20https://re.kufar.by/vi/{item['ad_id']}"

        try:
            request.urlopen(url)
        except:
            print('some exception: ' + town)