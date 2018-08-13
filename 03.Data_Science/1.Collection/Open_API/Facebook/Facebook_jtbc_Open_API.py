import urllib.request
import json
import sys

page_name = "jtbcnews"
app_id = "1996816077198504"
app_secret = "eab22761aaa199b79ec6509d620290d3"

def get_jtbc_news_page_ID():
    access_token = app_id + "|" + app_secret

    base = "https://graph.facebook.com/v2.8"
    node = "/" + page_name
    parameters = "/?access_token=%s" % access_token

    url = base + node + parameters

    req = urllib.request.Request(url)
    print("The request url for jtbc news ID: " + url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = json.loads(response.read().decode('utf-8'))
            page_id = data['id']
            print("%s Facebook Numeric ID: %s" % (page_name, page_id))
    except Exception as e:
        print(e)

    return page_id


page_id = get_jtbc_news_page_ID()
from_date = "2018-01-24"
to_date = "2018-01-25"
num_statuses = "100"
access_token = app_id + "|" + app_secret

base = "https://graph.facebook.com/v2.8"
node = "/%s/posts" % page_id
fields = "/?fields=id,message,link,name,type,shares,reactions," + \
         "created_time,comments.limit(0).summary(true)" + \
         ".limit(0).summary(true)"
duration = "&since=%s&until=%s" % (from_date, to_date)
parameters = "&limit=%s&access_token=%s" % (num_statuses, access_token)
url = base + node + fields + duration + parameters
print("The request url for jtbc news: " + url)
req = urllib.request.Request(url)

try:
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        jsonResult = json.loads(response.read().decode('utf-8'))

    with open('%s_facebook_%s_%s.json' % (page_name, from_date, to_date), 'w', encoding='utf8') as outfile:
        str_ = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(str_)
        print('%s_facebook_%s_%s.json SAVED' % (page_name, from_date, to_date))

except Exception as e:
    print(e)

print("End")


