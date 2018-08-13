import os
import sys
import urllib.request
import datetime
import time
import json

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager,rc

access_key=""

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(),url))
        return None

