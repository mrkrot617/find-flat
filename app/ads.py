from urllib import request
from datetime import datetime
from json import loads


def get_json_response(request_url):
    with request.urlopen(request_url) as url:
        response = url.read()

    return loads(response)


def get_ads(json_object):
    ads_json = json_object['ads']
    ads = []

    for key in ads_json:
        ad_date = str(datetime.strptime(key['list_time'], '%Y-%m-%dT%H:%M:%SZ').date())

        ads.append({'ad_id': key['ad_id'],
                    'company_ad': key['company_ad'],
                    'ad_date': ad_date})

    return ads
