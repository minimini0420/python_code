import urllib.request
import json

page_name = "jtbcnews"
app_id = "1996816077198504"
app_secret = "eab22761aaa199b79ec6509d620290d3"
access_token = app_id + "|" + app_secret

base = "https://graph.facebook.com/v2.8"
node = "/" + page_name
parameters = "/?access_token=%s" %access_token

url = base + node + parameters

req = urllib.request.Request(url)
print("url:"+url)

try:
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        data = json.loads(response.read().decode('utf-8'))
        page_id = data['id']
        print("%s Facebook Numeric ID : %s"%(page_name,page_id))
except Exception as e:
    print(e)