from bs4 import BeautifulSoup

html='<td class = "title"><div class="tit3"><a href="/movie/bi/mi/basic.nhn?code=158191" title="1987">1987</a></div><td/>'

# <a title <= 마우스 타켓시 설명 메세지 출력

soup = BeautifulSoup(html,'html.parser')
print(soup)
tag = soup.td
print(tag)
tag = soup.div
print(tag)
tag = soup.a
print(tag)
print(tag.name)
print(tag.attrs)
print(tag.string)
print(tag.text)