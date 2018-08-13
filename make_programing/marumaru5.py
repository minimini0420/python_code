import requests
from bs4 import BeautifulSoup
import mechanicalsoup
import urllib
import os
import shutil
import time
import sys
import zipfile
import multiprocessing
from multiprocessing import Pool

def down_bar(a):
    if a < 10 :return '□□□□□□□□□□'
    elif 10 <= a < 20 : return '■□□□□□□□□□'
    elif 20 <= a < 30 :return '■■□□□□□□□□'
    elif 30 <= a < 40: return '■■■□□□□□□□'
    elif 40 <= a < 50:return '■■■■□□□□□□'
    elif 50 <= a < 60:return '■■■■■□□□□□'
    elif 60 <= a < 70:return '■■■■■■□□□□'
    elif 70 <= a < 80:return '■■■■■■■□□□'
    elif 80 <= a < 90:return '■■■■■■■■□□'
    elif 90 <= a < 100:return '■■■■■■■■■□'
    elif a == 100 : return '■■■■■■■■■■'

def zip(src_path, dest_file):
    with zipfile.ZipFile(dest_file, 'w') as zf:
        rootpath = src_path
        for (path, dir, files) in os.walk(src_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, rootpath)
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()

def rep(a):       #파일 이름 특수문자 처리
    rep=""
    b = ['\\','/',':','*','?','"','<','>','|',' ']
    for c in a:
        if c in b :
            c=''
            rep+=c
        else: rep+=c
    return rep

def download(url, file_name):             # 파일 저장 함수
    with open(file_name, "wb") as file:
        response = requests.get(url,headers={'referer':comic_URL})
        file.write(response.content)

hdr1 ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)'}
hdr2 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win32; x32)'}
hdr3 ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)'}
hdr4 ={'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
hdr5 ={'User_Agent': 'AppleWebKit/537.36 (KHTML, like Gecko)'}
hdr = 0

def get_link():       #첫페이지 파싱
    comic = []
    url_list =[]
    sub_list=[]

    tit1 = urllib.parse.quote(tit.encode('utf-8'))
    URL = 'http://marumaru.in/?r=home&c=1%2F40&m=bbs&bid=manga&cat=&sort=gid&orderby=asc&recnum=30&type=&iframe=&skin=&where=subject&keyword='+tit1
    html = requests.get(URL, headers=hdr1).text
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('div', attrs={'class': 'sbjx'})

    for i in links:
        url_list.append(i.find('a').get('href'))
        sub_list.append(i.find('a').text)

    for i in range(len(url_list)):
        print(str(i+1)+' : '+ sub_list[i])

    pick =input("\n받으실 만화의 번호를 선택하세요:")
    link = url_list[int(pick)-1]
    sub = sub_list[int(pick)-1]

    sel = input("1:전부받기 2:골라받기 3:이어받기\n입력:")
    if sel =='1':
        print("\n전체를 다운로드 중입니다...")
    else : print("\n%s의 목록을 불러오는 중입니다.."%sub)

    URL2 ='http://marumaru.in/'+link       #링크들어가서 2번째 페이지 파싱
    html2 = requests.get(URL2,headers=hdr3).text
    soup2 = BeautifulSoup(html2, 'lxml')
    thumnail = soup2.find_all("div",attrs={'id':'vContent'})

    for i in thumnail:
        try:os.mkdir('C:/Windows/Temp/marumaru')
        except:pass
        try:os.mkdir('C:/Windows/Temp/marumaru/%s'%rep(sub))
        except:pass
        aa = i.find_all("a",attrs={"target":"_blank"})    #링크들어가서 이미지 긁어오기

        for j in aa:
            if len(j.text) > 2:
                # print(j.text)
                comic.append(sub+list(j.attrs.values())[1]+'  '+j.text)

    if sel =='1':
        print("다운로드 준비중입니다..")
        comic = comic

    elif sel =='2':
        for i in range(len(comic)):
            print(str(i+1)+" : "+comic[i][comic[i].index('  ')+2:])
        sel1 =input("\n원하시는 화를 선택하세요:")
        print("\n다운로드 중입니다...")
        comic = [comic[int(sel1)-1]]

    elif sel =='3':
        for i in range(len(comic)):
            print(str(i+1)+" : "+comic[i][comic[i].index('  ')+2:])
        sel1 =input("\n몇화부터 이어받을지 선택하세요:")
        print("\n다운로드 중입니다...")
        comic = comic[int(sel1)-1:]

    return comic

def get_image(comic):
    global comic_URL
    comic_URL = comic[comic.index('h'):comic.index('  ')]
    comic_name = comic[comic.index('  ')+2:]
    comic_dir_name = comic[:comic.index('h')]

    page = mechanicalsoup.Browser().get(comic_URL)
    comic_content = page.soup.find_all('img', attrs={"class": "lz-lazyload"})
    count = 0
    for j in comic_content:
        try:os.mkdir('C:/Windows/Temp/marumaru/%s/%s' % (rep(comic_dir_name),rep(comic_name)))
        except:pass
        co = 'http://wasabisyrup.com' + j.get('data-src')
        download(co, 'C:/Windows/Temp/marumaru/%s/%s/%s.jpg' % (rep(comic_dir_name), rep(comic_name), count))
        down = int(((comic_content.index(j)+1)/len(comic_content))*100)
        sys.stdout.write('\r'+rep(comic_name)+' : '+str(down)+'%...')
        count+=1
    print("\n%s : 다운완료"%(rep(comic_name)))

    ##파일 압축
    zip('C:/Windows/Temp/marumaru/%s/%s'%(rep(comic_dir_name),rep(comic_name)),'C:/Windows/Temp/marumaru/%s/%s.zip'%(rep(comic_dir_name),rep(comic_name)))
    time.sleep(3)
    try:os.mkdir('marumaru')
    except:pass
    try:os.mkdir('marumaru/%s'%rep(comic_dir_name))
    except:pass
    try :
        shutil.move('C:/Windows/Temp/marumaru/%s/%s.zip'%(rep(comic_dir_name),rep(comic_name)),'marumaru/%s'%rep(comic_dir_name))

    except FileNotFoundError:
        pass
    return comic_dir_name

if __name__=='__main__':
    # On Windows calling this function is necessary.
    if sys.platform.startswith('win'):
        multiprocessing.freeze_support()

    while True:
        print("<<< 마루마루 다운로더 ver0.3 >>>")
        tit = input("\n제목을 입력하세요(0입력시 종료):")
        if tit == '0':
            break
        else: pass
        print("\n검색중입니다...\n")

        start_time = time.time()

        pool = Pool(processes=8)
        comic_dir_name = pool.map(get_image, get_link())[0]
        shutil.rmtree('C:/Windows/Temp//marumaru/%s' % rep(comic_dir_name))
        print('다운로드 완료')
        print("\n--- %s seconds ---\n" %(time.time() - start_time))