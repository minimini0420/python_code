import requests
from requests import get
import random
import time
from bs4 import BeautifulSoup
import multiprocessing
from multiprocessing import Pool
import sys
import os

def download(url, file_name):             # 파일 저장 함수
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

def get_link():
    URL_list = []
    URL=input("갤러리 주소를 입력하세요(0입력시 프로그램 종료):\n\n")
    if URL[:25] != 'http://gall.dcinside.com/' and URL != '0':
        print("\n제대로 입력하셈요\n")
        return get_link()
    if URL == '0':
        exit()
    else: pass
    pick = input("\n1. 일반글 2. 개념글 : ")
    max_page = input("\n첫페이지부터 몇페이지까지 긁으실건가요?(max:10페이지):")
    if int(max_page) > 10 :
        return get_link()
    print("\n짤 긁을 준비중...\n")

    for idx in range(1,int(max_page)+1):
        if pick == '1':
            icon = 'icon_pic_n'
            URL = URL + '&page=%s' % str(idx)
        elif pick == '2':
            icon = 'icon_pic_b'
            URL = URL + '&page=%s&exception_mode=recommend' % str(idx)
        else:
            print("\n?? 제대로 입력 하셈")
            return get_link()

        html = requests.get(URL,headers=hdr5).text
        soup = BeautifulSoup(html, 'lxml')
        imagelist = soup.find_all('a',attrs={"class":icon})
        gall_subject = soup.find_all('meta',attrs={"name":"title"})
        sub= list(gall_subject[0].attrs.values())[1]

        for i in imagelist:
            a= list(i.attrs.values())[0]
            inURL='http://gall.dcinside.com'+a
            URL_list.append(inURL+"  "+sub)

    return URL_list

def get_image(URL_list):
      sub = URL_list[URL_list.index('  ')+2:]
      inURL = URL_list[:URL_list.index('  ')]
      g_time = time.strftime("%Y%m%d",time.localtime(time.time()))
      if random.randint(1, 6) == 1:hdr = hdr1
      elif random.randint(1, 6) == 2:hdr = hdr2
      elif random.randint(1, 6) == 3:hdr = hdr3
      elif random.randint(1, 6) == 4:hdr = hdr4
      else:hdr = hdr5

      # proxies = {'http':'138.197.45.244:80'}

      html2 = requests.get(inURL,headers=hdr).text
      soup2 = BeautifulSoup(html2,'lxml')
      image_scorll = soup2.find_all("li",attrs={'class':'icon_pic'})


      for i in image_scorll:
          b = (list(i.a.attrs.values())[0])
          b = b.replace('download.php', 'viewimage.php')
          image_name = list(i.strings)[0]

          if os.path.isdir("짤방"):
              pass
          else:os.mkdir("짤방")

          if os.path.isdir("짤방/"+g_time+'_'+sub):
              pass
          else:os.mkdir("짤방/"+g_time+'_'+sub)
          download(b, '짤방/'+g_time+'_'+sub + '/' + image_name)
          print('[%s] 받고 있습니다..' % image_name)
      time.sleep(5)


hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr4 ={'User-Agent': 'Chrome/63.0.3239.132 Safari/537.36)'}
hdr5 ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
hdr = 0


if __name__=='__main__':
    # On Windows calling this function is necessary.
    while True:
        if sys.platform.startswith('win'):
            multiprocessing.freeze_support()

        start_time = time.time()
        print("<< 갤 짤 존나 긁어오기 ver0.5 >>\n")
        print("설명:갤에 있는 짤들을 최대 10페이지까지 싹다 긁어옵니다.\n")

        pool = Pool(processes=8)
        pool.map(get_image, get_link())
        print("\n다운로드 완료")

        print("\n--- %s seconds ---\n" % (time.time() - start_time))

