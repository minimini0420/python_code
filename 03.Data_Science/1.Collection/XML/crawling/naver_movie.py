import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

index = "index"

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('div',attrs={'class':'tit3'})
rank_changes = soup.findAll('td',attrs={'class':'range ac'})

result_name = []
for i in tags:
    div_tag = list(i.strings)
    if (div_tag[1]):
        result_name.append(div_tag[1])

result_change = []
for i in rank_changes:
    td_rank_change = list(i.strings)
    if (td_rank_change[0]):
        result_change.append(td_rank_change[0])

result = []
for i in range(len(result_name)):
    rank = int(i)+1
    movie_name = result_name[i]
    change = result_change[i]
    result.append([str(rank)] + [movie_name] + [change])

print(result_name)
print(result_change)
print(result)

print("START")
naver_movie_table = DataFrame(result, columns=('순위','영화명','변동폭'))
naver_movie_table.to_csv("naver_movie.csv",encoding="cp949",mode='w',index=False)
print("END")